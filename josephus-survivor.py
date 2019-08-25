#VAR1
def josephus_survivor1(n,k):
    warriors = [i for i in range(1, n+1)]
    current_k = k-1
    while 1 != len(warriors):
        while current_k > len(warriors)-1:
            current_k = (current_k - len(warriors))
        warriors = warriors[current_k+1:] + warriors[:current_k]
    return warriors[0]

#VAR2
def josephus_survivor2(n,k):
    warriors = [i for i in range(1, n+1)]
    current_k = k-1
    while 1 != len(warriors):
        while current_k > len(warriors)-1:
            current_k = (current_k - len(warriors))
        warriors.pop(current_k)
        current_k += k-1
    return warriors[0]


#VAR 3 NOT MINE, FROM BEST SOLUTIONS

def josephus_survivor(n,k):
    print([i for i in range(1, n+1)])
    r = 0
    for i in range(1, n+1):
        r = (r+k) % i
    print(r+1)
    return r+1

josephus_survivor(7, 3)#4
josephus_survivor(11, 19)#10
josephus_survivor(1, 300)#1
josephus_survivor(14, 2)#13
josephus_survivor(100, 1)#100)