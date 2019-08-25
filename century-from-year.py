#Century From Year
#https://www.codewars.com/kata/century-from-year/
#

def century(year):
    # Finish this :)
    if year%100 == 0:
        return year//100
    else:
        return (year//100) + 1

print(century(1705)) #18
century(1900) #19
century(1601) #17
century(2000) #20
century(356) #4
century(89) #1