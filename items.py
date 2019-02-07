from scrape import *

class Items(object):
    name = ""
    url = ""
    price = 0
    status = ""

    def __init__(self, name, url, price, status):
        self.name = name
        self.url = url
        self.price = price
        self.status = status

    def status_check(self):
        global out_of_stock
        if out_of_stock:
            self.status = "OUT OF STOCK"
        else:
            for items in green_text:
                if 'In stock ' in items:
                    self.status = "IN STOCK"

airpods = Items(product, airpods, price, status)
airpods.status_check()

item_update = ("Product: " + str(airpods.name) +
        "(" + str(airpods.price) + ")" +
        " is: " + str(airpods.status))
