import scrapy
from bookshell import items


class ShelfSpider(scrapy.Spider):
    name = "books"
    custom_settings = {
		"FEEDS":{
            "books.json":{"format":"json", "overwrite":"True"},
           },
    }

    def __init__(self, *args, **kwargs):
        super(ShelfSpider, self).__init__(*args, **kwargs)

        self.start_urls = []
        self.start_urls.append(kwargs.get('start_urls'))

    def parse(self, response):
        books = response.xpath('//*[@id="booksBody"]/tr')
        for book in books:
            book_item = items.bookItem()
            book_item['title'] = book.xpath('td[@class="field title"]/div/a/text()').get().strip()
            book_item['author'] = book.xpath('td[@class="field author"]/div/a/text()').get().strip()
            book_item['link'] = response.urljoin(book.xpath('td[@class="field title"]/div/a/@href').get())
            yield book_item
