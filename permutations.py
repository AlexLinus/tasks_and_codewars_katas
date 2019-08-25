#Permutations
#https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
import itertools


def permutations(string):
    result = sorted(set(''.join(x) for x in itertools.permutations(string, r=len(string))))
    print(result)
    return result

    #your code here
sorted(permutations('a'))#, ['a']);
sorted(permutations('ab'))#, ['ab', 'ba'])
sorted(permutations('aabb'))#, ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])