item_atlas = {}

## Helpers ---------------------------------------------------------------------

def _min_max_quality(item, inc):
    new_quality = item.quality + inc
    new_quality = min(new_quality, 50)
    new_quality = max(new_quality, 0)
    item.quality = new_quality


# Default method definition ----------------------------------------------------
def update_default(item):
    if item.sell_in > 0:
        _min_max_quality(item, -1)
    else:
        _min_max_quality(item, -2)


# Atlas definition -------------------------------------------------------------

## AGED BRIE
def update_brie(item):
    if item.sell_in > 0:
        _min_max_quality(item, 1)
    else:
        _min_max_quality(item, 2)
item_atlas["Aged Brie"] = update_brie

## SULFURE
def update_sulfure(item):
    item.quality = 80
item_atlas["Sulfuras, Hand of Ragnaros"] = update_sulfure

## BACKSTAGE
def update_backstage(item):
    if item.sell_in <= 0:
        item.quality = 0
    elif item.sell_in <= 5:
        _min_max_quality(item, 3)
    elif item.sell_in <= 10:
        _min_max_quality(item, 2)
    else:
        _min_max_quality(item, 1)
item_atlas["Backstage passes to a TAFKAL80ETC concert"] = update_backstage

## CONJURED
def update_conjured(item):
    if item.sell_in > 0:
        _min_max_quality(item, -2)
    else:
        _min_max_quality(item, -4)
item_atlas["Conjured Mana Cake"] = update_conjured
