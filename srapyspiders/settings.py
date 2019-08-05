BOT_NAME = 'gztspider'
SPIDER_MODULES = ['srapyspiders']
NEWSPIDER_MODULE = 'srapyspiders.spiders'  # 使用scrapy crawl genspider xxx 创建的默认爬虫目录

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/74.0.3729.169 Safari/537.36"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Scrapy下载执行的最大请求数 (default: 16)
# CONCURRENT_REQUESTS = 32

# Scrapy处理item的并发量  (default: 100)
# CONCURRENT_ITEMS = 100

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:

# 现有的最大请求数，对于任何单域同时进行 (default: 8)
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 现有的请求的最大数量的同时执行任何单一的IP (default: 0) 0表示忽略
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 默认开启, 禁止cookies，有些站点会从cookies中判断是否为爬虫
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# http默认请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# 爬虫中间件
# SPIDER_MIDDLEWARES = {
#    'srapyspiders.middlewares.SrapyspidersSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# 下载中间件
# DOWNLOADER_MIDDLEWARES = {
#    'srapyspiders.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'srapyspiders.pipelines.SrapyspidersPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True

# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
