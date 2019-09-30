"""爬虫任务计划表"""
from dispatcher.aps import edit

if __name__ == '__main__':
    info = {'信用中国黑名单-浙江': {'second': '5'}, '51job': {'second': '10'}}
    edit(info)
    print('任务计划表新建完成')