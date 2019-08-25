def josephus(items,k):
    warriors = [i for i in items]
    current_k = k-1
    result = []
    while 0 != len(warriors):
        while current_k > len(warriors)-1:
            current_k = (current_k - len(warriors))
        popped_warrior = warriors.pop(current_k)
        result.append(popped_warrior)
        current_k += k-1
    return result
    #your code here

josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)  # 1,2,3,4,5,6,7,8,9,10]
josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)  # 2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4)  # 'e', 's', 'W', 'o', 'C', 'd', 'r', 'a']
josephus([1, 2, 3, 4, 5, 6, 7], 3)  # 3, 6, 2, 7, 5, 1, 4
josephus([], 3)  # []