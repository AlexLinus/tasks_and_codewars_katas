#Тестовое задание zensofta, решил через if else и цикл for. Другой вариант.
#Дан список ходов Стрелка вверх, стрелка вниз, вправо, влево. Узнать, вернется ли робот на начальную точку пройдя весь список.

steps_list_even = ['↓', '↑', '→', '←', '↓', '↑', '→', '←', '↓', '↑', '→', '←'] #even list
steps_list_odd = ['↓', '↑', '→', '←', '↓',  '→', '↓', '↑', '→', '←'] #odd list
steps_list_random = ['↓', '↑', '→', '←', '↓', '↑', '→', '←', '↓', '↑', '→', '←', '↓', '↑', '→', '←', '↓', '↑', '→', '←', '↓', '↑', '→', '←']

def check_position(steps_list):
    #print([True if steps_list.count(step)%2==0 else False for step in steps_list])
    return True if len(set([steps_list.count(step) for step in steps_list])) <=1 else False

print(check_position(steps_list_even))
print(check_position(steps_list_odd))
print(check_position(steps_list_random))