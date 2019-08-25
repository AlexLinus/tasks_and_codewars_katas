#https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python
# Write the function that parses the mileage number input, and returns a 2 if the number is "interesting"
#  (see below), a 1 if an interesting number occurs within the next two miles,
#  or a 0 if the number is not interesting.

# Any digit followed by all zeros: 100, 90000 - OK!
# Every digit is the same number: 1111 - OK!
# The digits are sequential, incementing†: 1234 - OK!
# The digits are sequential, decrementing‡: 4321 - OK!
# The digits are a palindrome: 1221 or 73837  OK!
# The digits match one of the values in the awesome_phrases array - OK!

def is_interesting(number, awesome_phrases):
    result = 0
    nums = [number+i for i in range(0,3)]
    if number+2 >= 100:
        def is_interesting_inner(number, awesome_phrases):
            def sequential(num_sample):
                print(num_sample)
                if str(num_sample) in '98765432101234567890':
                    return True
                else:
                    return False

            incementing = sequential(number)
            decrementing = sequential(number)

            if number in awesome_phrases:
                result = 2
            elif str(number).count(str(number)[0]) == len(str(number)) or str(number).count('0') == len(str(number))-1:
                result = 2
            elif str(number) == str(number)[::-1]:
                result = 2

            elif (decrementing == True or incementing == True) and number > 100:
                result = 2
            else:
                result = 0
            return result

        for num in nums:
            if num >99:
                result = is_interesting_inner(num, awesome_phrases)
                if result in [1,2]:
                    if num == nums[0]:
                        result = 2
                    else:
                        result = 1
                    break
    print('Результат: {}'.format(result))
    return result

is_interesting(99, [])