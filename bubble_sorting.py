#Пузырьковая сортировка.
#АЛГОРИТМ

input_list = [1,2,5,3,4,6,7,9,8]

def buble_sorting1(input_list):
    for item in input_list:
        for i in range(0, len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
            print(input_list)
    print(f'Результат: {input_list}')
    return input_list
#input_list.reverse()


def bubble_sorting2(input_list):
    a = input_list
    for i in range(len(a),0,-1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
        print(a)
    return a

bubble_sorting2(input_list)
