#Stringy Strings
#https://www.codewars.com/kata/stringy-strings/

def stringy(size):
    result = '1'
    while len(result) != size:
        if result[-1] == '1':
            result += '0'
        else:
            result += '1'
    print(result)
    return result
    # Good Luck!

stringy(3)  # , '101'
stringy(5)  # , '10101'
stringy(12)  # , '101010101010'
stringy(26)  # , '10101010101010101010101010'