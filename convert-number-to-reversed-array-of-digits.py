#8KY for noobs
#convert-number-to-reversed-array-of-digits
#https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/

def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]

digitize(35231) #[1,3,2,5,3]