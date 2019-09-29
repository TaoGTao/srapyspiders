"""爬虫任务计划表"""
from dispatcher.aps import edit

if __name__ == '__main__':
    info = {'51job': {'second': 5}, '信用中国黑名单-浙江': {'second': 2}}
    edit(info)
    print('任务计划表新建完成')