# Scrapy settings for songhelper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'songhelper'

SPIDER_MODULES = ['songhelper.spiders']
NEWSPIDER_MODULE = 'songhelper.spiders'
DOWNLOAD_DELAY = 1
#LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
