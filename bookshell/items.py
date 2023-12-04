from scrapy import Item, Field


class shelfItem(Item):
    name = Field()
    number = Field()
    link = Field()

class bookItem(Item):
    title = Field()
    author = Field()
    link = Field()