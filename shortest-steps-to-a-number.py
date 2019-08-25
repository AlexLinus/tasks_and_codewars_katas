#https://www.codewars.com/kata/shortest-steps-to-a-number/train/python
#Shortest steps to a number

def shortest_steps_to_num(num):
    # Good Luck!
    count = 0
    while num != 1:
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
    print(count)
    return count

shortest_steps_to_num(1) # 0
shortest_steps_to_num(12) # 4
shortest_steps_to_num(16) # 4
shortest_steps_to_num(71)# 9