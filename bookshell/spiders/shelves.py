import scrapy
from bookshell import items


class ShelfSpider(scrapy.Spider):
    name = "shelves"

    custom_settings = {
		"FEEDS":{
            "shelves.json":{"format":"json", "overwrite":"True"},
           },
    }
    def __init__(self, *args, **kwargs):
        super(ShelfSpider, self).__init__(*args, **kwargs)
        self.username = kwargs.get('username')

        self.start_urls = [
                f"https://www.goodreads.com/{self.username}",
        ]

    def parse(self, response):
        shelves = response.xpath('//*[@class="shelfContainer"]/a')
        for shelf in shelves:
            shelf_item = items.shelfItem()
            shelf_item['name'] = shelf.xpath("text()").get().strip().split('\u200e')[0]
            shelf_item['number'] = int(shelf.xpath("text()").get().split('(')[1].split(')')[0])
            shelf_item['link'] = response.urljoin(shelf.xpath("@href").get())
            yield shelf_item
