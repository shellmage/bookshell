import scrapy
from bookshell import items


class ShelfSpider(scrapy.Spider):
    name = "shelves"

    username = "shellmage"

    start_urls = [
            f"https://www.goodreads.com/{username}",
    ]

    def parse(self, response):
        shelves = response.xpath('//*[@class="shelfContainer"]/a')
        for shelf in shelves:
            shelf_item = items.shelfItem()
            shelf_item['name'] = shelf.xpath("text()").get().strip().split('\u200e')[0]
            shelf_item['number'] = shelf.xpath("text()").get().split('(')[1].split(')')[0]
            shelf_item['link'] = response.urljoin(shelf.xpath("@href").get())
            yield shelf_item
