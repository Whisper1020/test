# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GushiwenPipeline:
    fp = None
    #重写父类的一个方法
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./gushi.txt','w',encoding='utf8')

    #专门用来处理item类型对象：
    def process_item(self, item, spider):
        title = item['title']
        name_author = item['name_author']
        self.fp.write(title+':'+name_author+'\n')
        return item

    def close_spider(self,spider):
        print('爬虫结束')
        self.fp.close()
