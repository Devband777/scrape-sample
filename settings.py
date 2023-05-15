

BOT_NAME = 'phonehousebd'

SPIDER_MODULES = ['phonehousebd.spiders']
NEWSPIDER_MODULE = 'phonehousebd.spiders'


ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 32

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
   'phonehousebd.pipelines.PhonehousebdPipeline': 300,
}
POSTGRES_HOST = 'localhost'
POSTGRES_DATABASE = 'gsmbdphones'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'admin'
POSTGRES_TABLE = 'phones'
