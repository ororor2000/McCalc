
from importlib.util import resolve_name
from pydoc import resolve
import re
import sys
from models.McItem import McItem

class McManager:
    def __init__(self, data):
        self.menu = self.to_array(data)
    
    def to_array(self, data):
        list = []

        for i in range(len(data)):            
            list.append(McItem().to_object(data[i]))
        
        return list
    
    #returns tuple (full_list, standalone_list)
    def seperate_sub_type(self, items):
        standalone = []
        full = []

        for i in range(len(items)):
            if (items[i].sub_type == "standalone"):
                standalone.append(items[i])
            else:
                full.append(items[i])
        
        return (full, standalone)

    def ids_to_list(self, ids):
        items = []

        for i in range(len(ids)):
            id = ids[i]
            items.append(lambda x:x.id == id)
        
        return items
    
    def calulate_cheap_full(self, full, meal_size):
        prices = []

        for i in range(len(full)):
            price = 0

            for j in range(len(full)):
                if (i == j):
                    price += self.resolve_meal_size(full[i], meal_size)
                else:
                    price += full[i].price
            
            prices.append(price)

        return min(prices)

    #0 - regualr, 1 - big, 2/anything else - huge
    def resolve_meal_size(self, item, meal_size):
        if (meal_size == 0):
            return item.meal_price
        elif (meal_size == 1):
            return item.meal_price_big
        else:
            return item.meal_price_huge

    def build_order(self, ids, meal_size):
        items = self.ids_to_list(ids)

        tuple = self.seperate_sub_type(items)
        full = tuple[0]
        standalone = tuple[1]

        min_price = self.calulate_cheap_full(full, meal_size)
        min_index = full.index(min_price)
        
        return { "meal_item": full[min_index], "regular_items": (full.pop(min_index) + standalone)}

