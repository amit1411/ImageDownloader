# -*- coding: utf-8 -*-
import scrapy
from ..items import MyImage
import base64

class RedbubSpider(scrapy.Spider):
    name = 'ImageDownloader'
    allowed_domains = ['Website_Domain']
    start_urls = ['Website_URL']

    def parse(self, response):
        links = response.css('#masonrycontainer .bold a::attr(href)').extract()
        for link in links:
            url = response.urljoin(link)
            yield scrapy.Request(url=url, callback=self.parse_data)
        next_page = response.css('.pagination a[title*="Next Page"]::attr(href)').extract_first()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_data(self, response):
        image_data = MyImage()
        image_data["Creator"] = response.css('.pull-left span::text').extract_first()
        image_data["Name"] = ''.join(response.css('.well-inline h2::text').extract()).strip()
        a_img = ["NA"]
        img_urls = response.css('a[rel="carouselbits"]::attr(href)').extract_first()
        img_urls = response.urljoin(img_urls)
        a_img[0] = img_urls
        titles = response.css('a[rel="carouselbits"]::attr(title)').extract()
        # img_urls = [response.urljoin(i) for i in img_urls]
        image_data["image_urls"] = a_img
        # image_data["title"] = titles
        image_data["Description"] = ''.join(response.xpath('//*[@id="downloadDescription"]//text()').extract()).strip()
        try:
            image_names = img_urls.split("/")[-1]
        except IndexError:
            image_names = image_data["Creator"]
        # image_names = [i.split("/")[-1] for i in img_urls]
        try:
            image_data["category2"] = response.css('.breadcrumb li a::text').extract()[1]
            image_data["category3"] = response.css('.breadcrumb li a::text').extract()[2]
        except IndexError:
            image_data["category2"] = "NA"
            image_data["category3"] = "NA"
        image_data["category4"] = response.css('.hidden-phone::text').extract_first(default="NA")
        image_data["Expansion_Stuff_packs_required"] = response.css('.infobox .well-small p img::attr(alt)').extract() + response.css('.inlinepopover::text').extract()
        try:
            image_data["Downloads"] = response.css('.noborder .well-small .font-large *::text').extract()[1]
        except IndexError:
            image_data["Downloads"] = "NA"
        tags = response.css('#threadtagsarea a::text').extract()
        tags = ["#"+i for i in tags]
        image_data["Tags"] = tags if tags else "NA"
        data_1 = response.css('.infobox .well-small p span[class="bold"]::text').extract()
        info_box = {}
        for i in range(len(data_1)):
            info_box[data_1[i]] = response.css('.infobox .well-small em a::text').extract()[i]
        image_data["Infobox"] = info_box if info_box else "NA"
        # image_data["image_name"] = titles
        image_data["Image_Names"] = image_names
        image_data["Link"] = response.url
        yield image_data
