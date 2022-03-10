class McItem:
    def __init__(self, id = "", type = "", sub_type = "", child_option = False, category = "", title = "", price = 0, meal_price = 0, meal_price_big = 0, meal_price_huge = 0):
       self.id = id
       self.type = type
       self.sub_type = sub_type
       self.child_option = child_option
       self.category = category
       self.title = title
       self.price = price
       self.meal_price = meal_price
       self.meal_price_big = meal_price_big
       self.meal_price_huge = meal_price_huge
    
    def to_object(self, obj):
        return McItem(id = obj["id"], type = obj["type"], sub_type = obj["sub_type"], category = obj["category"], title = obj["title"], price = obj["price"], meal_price = obj["meal_price"], meal_price_big = obj["meal_price_big"], meal_price_huge = obj["meal_price_huge"])

