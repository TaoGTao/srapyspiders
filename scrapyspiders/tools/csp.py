from functools import reduce


def setting_plus(*settings):
    def add(setting1, setting2):
        new_setting = setting1.copy()
        for s in setting2:
            if s not in setting1:
                new_setting[s] = setting2[s]
            elif isinstance(setting2[s], dict):
                new_setting[s] = add(setting1[s], setting2[s])
            elif setting2[s] == setting1[s]:
                pass
            else:
                raise ValueError("非字典类型的同名setting不能合并 %s" % str(s))
        return new_setting

    return reduce(add, settings)


def ll_extra_settings(*extra):
    return setting_plus(log_default_settings, ll_download_pipe_settings, *extra)


def get_middleware_setting(middleware, index=100):
    """
    :param middleware: 中间件
    :param index: 中间件序号，默认100
    :return:
    """
    return {"DOWNLOADER_MIDDLEWARES": {middleware.__module__ + '.' + middleware.__name__: index}}


ll_download_pipe_settings = {"ITEM_PIPELINES": {'scrapyProj.pipelines.LLDownloadPipe': 7, }}

log_default_settings = {"LOG_FILE": ""}

validate_settings_1 = {
    "DOWNLOADER_MIDDLEWARES": {
        'scrapyProj.middlewares.MyValidateMiddleWare': 131,
    },
}

fixed_user_agent_middleware = {
    "DOWNLOADER_MIDDLEWARES": {
        'scrapyProj.middlewares.agent.FixedAgent': 132,
    },
}

ll_default_settings = ll_extra_settings()


def get_download_delay(delay=2):
    return {"DOWNLOAD_DELAY": delay}


def get_concurrent_requests(count=1):
    return {"CONCURRENT_REQUESTS": count}


def get_handle_httpstatus_list(codes):
    if isinstance(codes, int):
        codes = [codes]
    return {"HTTPERROR_ALLOWED_CODES": codes}


FIXED_PROXY = "fixed_proxy"
WAN_PROXY = "wan_proxy"
SPIDER_PROXY = "spider_proxy"


def get_proxy_setting(mode=FIXED_PROXY, **kwargs):  # middleware的顺序，处理request由小及大，处理response由大及小
    if mode == FIXED_PROXY:
        return {
            FIXED_PROXY: kwargs.get("proxy"),
            "DOWNLOADER_MIDDLEWARES": {
                'scrapyProj.middlewares.proxy.FixedProxy': 553,
            },
        }
    if mode == WAN_PROXY:
        return {
            "DOWNLOADER_MIDDLEWARES": {
                'scrapyProj.middlewares.proxy.WanProxy': 553,
            },
            "start_with_proxy": kwargs.get("start_with_proxy", True)
        }
    if mode == SPIDER_PROXY:
        return {
            "DOWNLOADER_MIDDLEWARES": {
                'scrapyProj.middlewares.proxy.SpiderProxy': 553,
            }
        }


def get_my_retry_settings(func, code=403, RETRY_TIMES=None):
    info = {
        "DOWNLOADER_MIDDLEWARES": {
            'scrapyProj.middlewares.retry.ChangeStatusCodeMiddleWare': 554,
        },
        "change_status_code_func": func,
        "change_status_code_code": code,
    }
    if RETRY_TIMES:
        info.update({"RETRY_TIMES": RETRY_TIMES})
    return info
