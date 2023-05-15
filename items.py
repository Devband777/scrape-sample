
import scrapy


class PhonehousebdItem(scrapy.Item):

    def __setitem__(self, key, value):
        self._values[key] = value
        self.fields[key] = {}

