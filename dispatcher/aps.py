import datetime
import subprocess
import json
from apscheduler.schedulers.blocking import BlockingScheduler
from dispatcher.mq import AmqPoster

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                      datefmt='%Y-%m-%d %H:%M:%S',
#                      filename='log.txt',
#                     filemode='a')

queue_info = ("test", ('guest', 'guest'), dict(host='127.0.0.1', port=5672), '/')

def start_spider(name): # 爬虫生产模块
    command = [
        "cd ..\srapyspiders",
        "scrapy crawl %s" % name,
    ]
    subprocess.run(" && ".join(command), shell=True)

def sched(ch, method, properties, body): # 调度
    # print(body)
    # print(type(body))
    di = json.loads(body.decode())
    scheduler = BlockingScheduler()
    for k, v in di.items():  # 将调度任务写到redis中
        print(k, v)
        scheduler.add_job(func=start_spider, args=(k,), trigger='cron', **v)
        # scheduler.add_job(func=aps_test, args=('一次性任务',),
        #                   next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
        # scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=12)
        # scheduler._logger = logging
        # scheduler.add_listener(my_listener)
    scheduler.start()


def cs():  # 消费者
    mq = AmqPoster(*queue_info)
    mq.consume(sched)
    mq.close()

def edit(info):  # 任务计划生产者
    mq = AmqPoster(*queue_info)
    mq.send(json.dumps(info, ensure_ascii=False))
    mq.close()


if __name__ == '__main__':
    cs()
