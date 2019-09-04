import re
import os
import scrapyspiders

def get_spider_path(path):
    """
    :param path:
    :return: 文件绝对路径
    """
    return 'scrapyspiders.' + os.path.relpath(path, scrapyspiders.__path__[0]).replace(".py", "").replace(os.sep, ".")