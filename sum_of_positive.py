#8KY for noobs
#Sum of positive
#You get an array of numbers, return the sum of all of the positives ones.
#https://www.codewars.com/kata/5715eaedb436cf5606000381/

def positive_sum(arr):
    # Your code here
    return sum([i for i in arr if i>0])


positive_sum([1,-2,3,4,5]) #,13