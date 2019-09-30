import json
import subprocess
from threading import Thread

from apscheduler.schedulers.blocking import BlockingScheduler

from dispatcher.databaseconfig import queue_info
from dispatcher.mq import AmqPoster

scheduler = BlockingScheduler()


def start_spider(name):  # 爬虫生产模块
    command = [
        "scrapy crawl %s" % name,
    ]
    subprocess.run(" && ".join(command), shell=True)


def sched(di):  # 调度
    di = json.loads(di)
    for k, v in di.items():
        scheduler.add_job(func=start_spider, args=(k,), trigger='cron', **v)
    return True


def cs():  # 消费者
    amq = AmqPoster(*queue_info)
    amq.consume(sched, lambda: True)
    Thread(target=scheduler.start).start()
    amq.consume(lambda x: False, lambda: True)
    amq.close()
    scheduler.shutdown(wait=True)
    subprocess.run('git pull', shell=True)
    raise Exception("监听到发生了变化，重启")


def edit(info):  # 任务计划生产者
    mq = AmqPoster(*queue_info)
    mq.send(json.dumps(info, ensure_ascii=False))
    mq.close()


if __name__ == '__main__':  # 线上supervisor 自动重启
    cs()
