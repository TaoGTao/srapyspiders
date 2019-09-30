import subprocess
import time

command = "python D:/gzt/新环境/测试专用/分布式爬虫调度管理系统/srapyspiders/dispatcher/aps.py"  # 注意命令行路径问题

if __name__ == '__main__':
    p = subprocess.Popen(command, shell=True)
    try:
        while 1:
            time.sleep(5)
            if p.poll() is None:  # 判断程序进程是否存在，None：表示程序正在运行 其他值：表示程序已退出
                pass
            else:
                print('即将开始重启')
                p = subprocess.Popen(command, shell=True)
    except KeyboardInterrupt as e:
        print("检测到CTRL+C，准备退出程序!")
