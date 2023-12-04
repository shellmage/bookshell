import scrapy
from bookshell import items


class ShelfSpider(scrapy.Spider):
    name = "books"

    start_urls = [
            f"https://www.goodreads.com/review/list/91502210?shelf=read",
    ]

    def parse(self, response):
        books = response.xpath('//*[@id="booksBody"]/tr')
        for book in books:
            book_item = items.bookItem()
            book_item['title'] = book.xpath('td[@class="field title"]/div/a/text()').get().strip()
            book_item['author'] = book.xpath('td[@class="field author"]/div/a/text()').get().strip()
            book_item['link'] = response.urljoin(book.xpath('td[@class="field title"]/div/a/@href').get())
            yield book_item
