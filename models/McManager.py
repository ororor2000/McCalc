
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
            item = next((x for x in self.menu if x.id == id), None)
            items.append(item)
        
        return items
    
    def calulate_cheap_full(self, full, meal_size):
        prices = []

        for i in range(len(full)):
            price = 0

            for j in range(len(full)):
                if (i == j):
                    price += self.resolve_meal_size(full[j], meal_size)
                else:
                    price += full[j].price
            
            prices.append(price)

        min_val = min(prices)

        return (prices.index(min_val), min_val)

    #0 - regualr, 1 - big, 2 - huge
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
        
        calcation_tuple = self.calulate_cheap_full(full, meal_size)
        min_index = calcation_tuple[0]        
        total_price = calcation_tuple[1]

        for i in range(len(standalone)):
            total_price += standalone[i].price

        l = full

        result =  { "meal_item": full[min_index], "regular_items": ([l.pop(min_index)] + standalone), "total_price": total_price}

        return result

