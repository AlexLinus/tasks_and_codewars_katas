#https://www.codewars.com/kata/perimeter-of-squares-in-a-rectangle/train/python
#The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80
#Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:
#The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.
#Fibonacci use
#https://www.codewars.com/kata/perimeter-of-squares-in-a-rectangle/train/python Посмотреть свежей головой, почему так. ПОчему умножаем на 4 ,если считаем 2 блока с длиной 1, а не 1 блок с длиной 1.
def perimeter(n):
    count = 0
    fib_list = []
    a, b = 0, 1
    while count != n+1:
        count += 1
        fib_list.append(b)
        a, b = b, b+a
    print(b)
    print(fib_list)
    return 4*sum(fib_list)
    # your code

perimeter(5) == 80
#perimeter(7) == 216
#perimeter(20) == 114624
#perimeter(30) == 14098308
#perimeter(100) == 6002082144827584333104