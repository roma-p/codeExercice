# -*- coding: utf-8 -*-
from item_atlas import item_atlas, update_default

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.item_atlas = item_atlas

    def defaut_quality_update(sef, item):
        return update_default(item)

    def update_quality(self):
        for item in self.items:
            if item.name not in self.item_atlas:
                self.defaut_quality_update(item)
            else:
                self.item_atlas[item.name](item)
            item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
