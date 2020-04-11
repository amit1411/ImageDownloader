# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyImage(scrapy.Item):
    # title = scrapy.Field()
    # createDate = scrapy.Field()
    image_urls = scrapy.Field()
    # images = scrapy.Field()
    Creator = scrapy.Field()
    Name = scrapy.Field()
    Description = scrapy.Field()
    category2 = scrapy.Field()
    category3 = scrapy.Field()
    category4 = scrapy.Field()
    Expansion_Stuff_packs_required = scrapy.Field()
    Downloads = scrapy.Field()
    Tags = scrapy.Field()
    Image_Names = scrapy.Field()
    Infobox = scrapy.Field()
    Link = scrapy.Field()
    # image_name = scrapy.Field()
