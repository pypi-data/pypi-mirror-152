# 环境要求
    python3.7 及以上 pip install lettuce-Dtester
# 新增指令
    --lf, --ff, --cc, --tn II --last-failed, --failed-first, --clear-cache, --task-name

    --lf: 仅执行上次未通过的测试案例

    --ff: 优先执行未通过的测试案例，通过的测试案例滞后执行

    --cc: 清除case_cache

    --tn: 在不与其他三个命令一起使用时指的是指定任务目录即 festures文件夹下的目录

    --lf --tn task_name: 仅执行指定任务的未通过案例

    --ff --tn task_name: 优先执行执行指定任务的未通过案例

    --cc --tn task_name: 删除指定任务所有缓存文件，再次执行

    --cc --lf --tn task_name: 会报错，因为会优先删除缓存文件，删除后无法支持--lf指令

    --cc --ff --tn task_name: 会报错，因为会优先删除缓存文件，删除后无法支持--ff指令

# 目录信息
    在根目录下生成case_cache目录
    目录结构如下：（以本次执行案例文件夹为features/fee_test举例）
    |---case_cache
        |---{task_name}_cache
            |---{task_name}(保存本次执行的py文件，用于后续的--ff, --lf执行)
                |---...py(指代保存的py文件)
            |---run_res(保存执行结果)
                |---error_case.feature（保存出错或跳过的案例原文）
                |---failed_first_case.feature(保存全部案例，但是出错的测试案例在前面)
                |---res.txt(保存错误或跳过的测试案例原始信息包含报错详情)
            |---lf_res(保存lf执行后结果，不执行lf命令不生成)
                |---error_case.feature
                |---failed_first_case.feature
                |---res.txt
            |---ff_res(保存ff执行后结果，不执行ff命令不生成)
                |---error_case.feature
                |---failed_first_case.feature
                |---res.txt
    

# 使用方法
    在项目根目录下存在mian.py/run.py作为入口:

    import lettuce
    import os
    
    
    class HtmlRunner(lettuce.Runner):
        def __init__(self, base_path, enable_html=False, html_filename=None, enable_email=False, recipients=None,
                     smtp_host=None, smtp_port=None, credential=None, *args, **kwargs):
            lettuce.Runner.__init__(self, base_path, *args, **kwargs)
    
    
    def test_a():
        run_path = lettuce.run_task('case_a')
        base_path = os.path.join(os.path.dirname(os.curdir),
                                 run_path)  # the path of .py and .feature
        lettuce.world.task_path = base_path
        tests_runner = HtmlRunner(base_path,
                                  enable_html=True,
                                  tags=("run",),
                                  enable_xunit=True,
                                  verbosity=4)
        tests_runner.run()
    
    
    if __name__ == '__main__':
        test_a()



# 修改信息

    新增文件：cacheprovider.py

    修改lettuce：__init__.py 引用：

    from lettuce.cacheprovider import  build_failed_first_case, run_task

    修改lettuce/plugins/colored_shell_output.py 文件获取案例信息


    def wp(l):
        if l.startswith("\033[1;32m"):
            l = l.replace(" |", "\033[1;37m |\033[1;32m")
        if l.startswith("\033[1;36m"):
            world.skip_flag = True
            l = l.replace(" |", "\033[1;37m |\033[1;36m")
        if l.startswith("\033[0;36m"):
            world.skip_flag = True
            l = l.replace(" |", "\033[1;37m |\033[0;36m")
        if l.startswith("\033[0;31m"):
            world.fail_flag = True
            l = l.replace(" |", "\033[1;37m |\033[0;31m")
        if l.startswith("\033[1;30m"):
            l = l.replace(" |", "\033[1;37m |\033[1;30m")
        if l.startswith("\033[1;31m"):
            world.fail_flag = True
            l = l.replace(" |", "\033[1;37m |\033[0;31m")   
        return l
    
    
    def wrt(what):
        if six.PY2:
            if isinstance(what, unicode):
                what = what.encode('utf-8')
        if six.PY3:
            if isinstance(what, bytes):
                print(what)
                what = what.decode('utf-8')
        world.case.append(what)
        sys.stdout.write(what)

    修改registry.py生成缓存
    增加build_case方法
    def case_data():
        temp_list = list()
        _case = world.case[:]
        for i in _case:
            a = i.replace("\033[1;37m", '')
            a = a.replace("\033[1;32m", '')
            a = a.replace("\033[1;30m", '')
            a = a.replace("\033[0m", '')
            a = a.replace("\033[A", '')
            a = a.replace("\033[0;36m", '')
            if not a.startswith("Feature"):
                if a in temp_list:
                    ...
                else:
                    temp_list.append(a)
                    yield a

    def build_case(scenario):
    
        if world.fail_flag is True or world.skip_flag is True:
            with open(f'{world.cache_path}/res.txt', 'a+', encoding='utf8') as f:
                with open(f'{world.cache_path}/error_case.feature', 'a+', encoding='utf8') as c:
                    for a in case_data():
                        # 收集错误案例详情，支持-lf指令执行上次失败的案例
                        if "\033[0;31m" not in a and "\033[1;31m" not in a:
                            if "#" in a:
                                c.write(a.split('#')[0].rstrip() + '\n')
                            elif "|" in a:
                                c.write(a)
                        # 收集错误信息，保存在结果文件
                        a = a.replace("\033[0;31m", 'error!')
                        a = a.replace("\033[1;31m", 'error!')
                        a = a.replace("\033[1;41;33m", '')
                        f.write(f'{a}\n')                        
        else:
            with open(f'{world.cache_path}/temp_case.feature', 'a+', encoding='utf8') as t:
                for a in case_data():
                    if "#" in a:
                        t.write(a.split('#')[0].rstrip() + '\n')
                    elif "|" in a:
                        t.write(a)
        if world.fail_flag is True or world.skip_flag is True:
            world.case_log_name = int(time.time())
            with open(f'{world.cache_path}/res.txt', 'a+', encoding='utf8') as f:
                f.write(f'日志详情见：{world.case_log_name}')

        world.fail_flag = False
        world.skip_flag = False
        world.case = []
    修改CallbackDict类，在每次执行一条案例完成后增加构建缓存函数
    class CallbackDict(dict):
        def append_to(self, where, when, function):
            if not any(_function_matches(o, function) for o in self[where][when]):
                self[where][when].append(function)
                if where == 'scenario' and when == 'after_each':
                    self[where][when].append(build_case)

