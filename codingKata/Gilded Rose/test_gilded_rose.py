# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def _skip_days(day_nbr, gilded_rose):
        for day in range(day_nbr):
            gilded_rose.update_quality()

    def test_normal(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Stuffed", sell_in=3, quality=7),
        ]
        gilded_rose = GildedRose(items)

        GildedRoseTest._skip_days(2, gilded_rose)
        self.assertEqual(items[0].quality, 18)
        self.assertEqual(items[1].quality, 5)
        self.assertEqual(items[2].quality, 5)

        GildedRoseTest._skip_days(2, gilded_rose)
        self.assertEqual(items[0].quality, 16)
        self.assertEqual(items[1].quality, 3)
        self.assertEqual(items[1].quality, 3)

        GildedRoseTest._skip_days(2, gilded_rose)
        self.assertEqual(items[0].quality, 14)
        self.assertEqual(items[1].quality, 0)
        self.assertEqual(items[1].quality, 0)

    def test_brie(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=0),
        ]
        gilded_rose = GildedRose(items)
        GildedRoseTest._skip_days(1, gilded_rose)
        self.assertEqual(items[0].quality, 1)

        GildedRoseTest._skip_days(2, gilded_rose)
        self.assertEqual(items[0].quality, 4)

        GildedRoseTest._skip_days(100, gilded_rose)
        self.assertEqual(items[0].quality, 50)

    def test_sulfure(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        ]
        gilded_rose = GildedRose(items)
        GildedRoseTest._skip_days(100, gilded_rose)
        for item in items:
            self.assertEqual(item.quality, 80)

    def test_backstage(self):
        items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        ]
        gilded_rose = GildedRose(items)
        GildedRoseTest._skip_days(1, gilded_rose)
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[1].quality, 50)
        self.assertEqual(items[2].quality, 50)

        GildedRoseTest._skip_days(5, gilded_rose)
        self.assertEqual(items[0].quality, 27)
        self.assertEqual(items[1].quality, 50)
        self.assertEqual(items[2].quality, 0)

        GildedRoseTest._skip_days(3, gilded_rose)
        self.assertEqual(items[0].quality, 33)

        GildedRoseTest._skip_days(5, gilded_rose)
        self.assertEqual(items[0].quality, 47)

    def test_conjured(self):
        items = [
            Item(name="Conjured Mana Cake", sell_in=3, quality=20)
        ]
        gilded_rose = GildedRose(items)
        GildedRoseTest._skip_days(1, gilded_rose)
        self.assertEqual(items[0].quality, 18)
        GildedRoseTest._skip_days(3, gilded_rose)
        self.assertEqual(items[0].quality, 10)


if __name__ == '__main__':
    unittest.main()