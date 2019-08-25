#Reversed sequence
#8 ky for noobs
#https://www.codewars.com/kata/reversed-sequence/

def reverse_seq(n):
    #var2 list(reversed([i for i in range(1, n+1)])))
    return [i for i in range(1, n+1)][::-1]

reverse_seq(5) #[5,4,3,2,1]