# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from urllib.parse import urlparse


class ImageDownloaderPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        return 'files/' + os.path.basename(urlparse(request.url).path)
    #
    # def get_media_requests(self, item, info):
    #     return [scrapy.Request(x, meta={'image_name': item["image_name"]})
    #             for x in item.get('image_urls', [])]
    #
    # def file_path(self, request, response=None, info=None):
    #     return '%s.jpg' % request.meta['image_name']
