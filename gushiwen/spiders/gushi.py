import scrapy
from scrapy import cmdline
from gushiwen.items import GushiwenItem


class GushiSpider(scrapy.Spider):
    name = "gushi"
    # allowed_domains = ["www.gushiwen.cn"]
    start_urls = ["https://so.gushiwen.cn/gushi/tangshi.aspx"]

    def parse(self, response):
        # all_data = []
        div_list = response.xpath('//div[@class="left"]/div[@class="sons"]/div')
        # span_list = response.xpath('//div[@class="left"]/div[@class="sons"]/div/span')
        for div in div_list:
            title = div.xpath('./div/strong/text()')[0].extract()
            name_author = div.xpath('./span//text()').extract()
            name_author = ''.join(name_author)

            item = GushiwenItem()
            item['title'] = title
            item['name_author'] = name_author

            yield item
            # print(title,name_author)
            # break
            # dic = {
            #     'title': title,
            #     'name_auther': name_author
            # }
            # all_data.append(dic)

        # for span in span_list:
        #     name_author = span.xpath('.//text()').extract()
        #     name_author = ''.join(name_author)
        #     # print(name_author)
        #     # break

        # return all_data
        #进行测试
cmdline.execute('scrapy crawl gushi'.split())
# cmdline.execute('scrapy crawl gushi -o ./gushi.csv')