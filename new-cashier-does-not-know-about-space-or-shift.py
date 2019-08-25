def get_order(order):
    menu = ['Burger',  'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    result = []
    for menu_item in menu:
        if menu_item.lower() in order:
            count = order.count(menu_item.lower())
            while count != 0:
                result.append(menu_item)
                count -=1
    return ' '.join(result)

get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza") # "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke")
get_order("pizzachickenfriesburgercokemilkshakefriessandwich") #"Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke")