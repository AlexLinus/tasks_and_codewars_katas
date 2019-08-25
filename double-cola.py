def who_is_next(names, r):
    while r > len(names):
        r = (r - (len(names) - 1)) / 2
    print(names[int(r)-1])
    return names[int(r) - 1]
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


who_is_next(names, 1) # "Sheldon"
who_is_next(names, 52) # "Penny"
who_is_next(names, 7230702951) # "Leonard"
who_is_next(names, 5033) #Howard