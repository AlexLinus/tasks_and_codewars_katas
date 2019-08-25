def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

#print(is_prime(101))


def gap3(g, m, n):
    #Проверка является ли число простым. То есть мы делим от 2 до n-1, получается если будут 0 где-то, то значит оно делится кроме 1 и самого себя, а если будет везде остаток (не ноль), то значит оно не делится.
    simple_list = list(filter(is_prime, range(m, n)))

    result = []
    for i in range(0, len(simple_list)-1):
        if simple_list[i+1] - simple_list[i] == g:
            result.extend([simple_list[i], simple_list[i+1]])
            break
    print(result)
    return result

#VAR2 не прошёл performance test. Too slow. TL 12000 ms
def gap(g, m, n):
    #Проверка является ли число простым. То есть мы делим от 2 до n-1, получается если будут 0 где-то, то значит оно делится кроме 1 и самого себя, а если будет везде остаток (не ноль), то значит оно не делится.
    simple_list = [num for num in range(m, n+1) if all(num % i for i in range(2, num))]
    result = []
    for i in range(0, len(simple_list)-1):
        if simple_list[i+1] - simple_list[i] == g:
            result.extend([simple_list[i], simple_list[i+1]])
            break
    return result
    # your code

#gap(2, 100, 110)  # [101, 103]
#gap(4, 100, 110)  # [103, 107]
#gap(6, 100, 110)  # None
#gap(8, 300, 400)  # [359, 367]
gap(10, 300, 400)  # [337, 347]


#Варианты не мои
def gap(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g:
                return [previous_prime, i]
            previous_prime = i
    return None


def is_prime(n):
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0:
            return False
    return True


#Второй не мой вариант
def gap(g, m, n):
    prev = 2
    for x in range(m|1, n + 1, 2):
        if all(x%d for d in range(3, int(x**.5) + 1, 2)):
            if x - prev == g: return [prev, x]
            prev = x