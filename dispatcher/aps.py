import json
import subprocess
import time
from threading import Thread

from apscheduler.schedulers.blocking import BlockingScheduler

from dispatcher.db import get_redis
from dispatcher.mq import AmqPoster

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                      datefmt='%Y-%m-%d %H:%M:%S',
#                      filename='log.txt',
#                     filemode='a')

queue_info = ("test", ('guest', 'guest'), dict(host='127.0.0.1', port=5672), '/')
SECHEDULER = 'dispatcher:scheduler'
UPDATETIME = 'dispatcher:updatetime'

scheduler = BlockingScheduler()

def start_spider(name):  # 爬虫生产模块
    command = [
        "cd ..\srapyspiders",
        "scrapy crawl %s" % name,
    ]
    subprocess.run(" && ".join(command), shell=True)


def sched(di):  # 调度
    di = json.loads(di)
    for k, v in di.items():  # 将调度任务写到redis中
        try:
            scheduler.add_job(func=start_spider, args=(k,), trigger='cron', **v)
            get_redis().hset(SECHEDULER, k, v)
        except:
            get_redis().hset(SECHEDULER, k, '%s安装失败' % k)
            print('定时任务-%s 安装失败' % k)
    get_redis().set(UPDATETIME, time.time())
    return True
        # scheduler.add_job(func=aps_test, args=('一次性任务',),
        #                   next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
        # scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=12)
        # scheduler._logger = logging
        # scheduler.add_listener(my_listener)
    # scheduler.start()


def cs():  # 消费者
    amq = AmqPoster(*queue_info)
    get_redis().delete(SECHEDULER)
    get_redis().delete(UPDATETIME)
    amq.consume(sched, lambda: True)
    # 消费第一条mq消息初始化
    # 初始化完成后监听下一条mq消息，监听到即重启
    Thread(target=scheduler.start).start()  # 另起一个线程启动
    amq.consume(lambda x: False, lambda: True)
    amq.close()
    scheduler.shutdown(wait=True)
    get_redis().delete(SECHEDULER)
    get_redis().delete(UPDATETIME)
    subprocess.run('git pull', shell=True)
    raise Exception("监听到发生了变化，重启")


def edit(info):  # 任务计划生产者
    mq = AmqPoster(*queue_info)
    mq.send(json.dumps(info, ensure_ascii=False))
    mq.close()


if __name__ == '__main__':
    cs()
