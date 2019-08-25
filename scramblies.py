#Scramblies
#Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
#Performance required
#https://www.codewars.com/kata/scramblies/train/python

#VAR1
def scramble1(s1, s2):
    return True if all([True if i in s1 and s1.count(i) >= s2.count(i) else False for i in s2]) else False

#VAR2

def scramble2(s1, s2):
    # your code here
    s1, s2 = list(s1), list(s2)
    result = []
    for letter in s2:
        if letter in s1:
            s1.remove(letter)
            result.append(True)
        else:
            result.append(False)
    return True if all(result) else False

#VAR3 BEST PERFOMANCE
from collections import Counter

def scramble3(s1, s2):
    s1, s2 = Counter(s1), Counter(s2)
    return True if len({k: s1[k] for k in s2 if k in s1 and s2[k] <= s1[k]}) == len(s2) else False



#VAR4 NOT MINE, Borrowed from Best Solutions

def scramble4(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

print(scramble1('rkqodlw', 'world') == True)
print(scramble3('cedewaraaossoqqyt', 'codewars') == True)
print(scramble2('katas', 'steak') == False)
print(scramble3('scriptjava', 'javascript') == True)
print(scramble3('scriptingjava', 'javascript') == True)

print(scramble3('rkqodlw', 'world')) #True