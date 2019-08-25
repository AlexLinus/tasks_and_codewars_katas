def cakes(recipe, available):
    result_list = []
    for key in recipe:
        if key in available:
            result_list.append(available[key]/recipe[key])
        if key not in available:
            result_list.append(False)
    if False not in result_list:
        return round(min(result_list))
    else:
        return 0



#Не мой вариант
def cakes2(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0


#recipe = {"flour": 500, "sugar": 200, "eggs": 1}
#available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
#cakes(recipe, available)#, 2, 'Wrong result for example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)#, 0, 'Wrong result for example #2')

