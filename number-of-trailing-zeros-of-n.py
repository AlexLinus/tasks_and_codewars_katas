#number-of-trailing-zeros-of-n
#FACTORIAL
#https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/python
#https://javabypatel.blogspot.com/2017/05/count-trailing-zeros-in-factorial-of-number.html
from functools import reduce

#Var1 bad performance, but it works
def zeros1(n):
    num = reduce((lambda x, y: x * y), [i for i in range(1, n+1)]) if n >0 else 0
    result = 0
    print(num)
    if num > 0:
        for i in str(num)[::-1]:
            if i == '0':
                result +=1
            else:
                break
    print(result)
    return result

#NOT MINE
def zeros(n):
  x = n/5
  return int(x+zeros(x) if x else 0)




print(zeros(0))#, 0, "Testing with n = 0")
print(zeros(6))#, 1, "Testing with n = 6")
print(zeros(30))#, 7, "Testing with n = 30")