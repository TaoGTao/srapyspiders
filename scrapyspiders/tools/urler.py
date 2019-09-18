import re


def get_next_page(url, formart=None, first=None, fns="_", mod=1, dont_print=False, first_page_add=None, **kwargs):
    """
    拼接的方式获取下一页url
    :param first_page_add: 首页常常会省略如index.html的后缀，而这对于后续页面有用，需要人工加上
    :param dont_print: 打印当前页码的开关
    :param mod: 每次翻页加几
    :param fns: 第一页和第二页等区别的字符
    :param url: 当前页url
    :param formart: 改变部分的格式%d是必选项，表示页码 （这里拼错了，将错就错吧）
    :param first: 第一页符合格式，填None 否则填第一页对应的页码0或1
    :return:
    """

    def get_page(s):
        page = int(s) + mod
        if not dont_print:
            print("获取到第%d页链接" % (page // mod))
        return page

    if url.endswith("/"):
        url += first_page_add or ""

    if formart is None:
        formart = "index_%d.html"
    if first is None:
        re_string = formart.replace("%d", "(\d+)")
        return re.sub(re_string, lambda x: formart % (get_page(x.group(1))), url)
    re_string = formart.replace(fns + "%d", "(?:" + fns + "(\d+))?")
    return re.sub(re_string, lambda x: formart % (get_page((x and x.group(1)) or first)), url)
