import time, math
start_time = time.time()
def prime_factor(number):
    if number == 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        r = math.floor(number // 2)
        f = 5
        while f <= r:
            if number % f == 0:
                return False
            if number % (f+2) == 0:
                return False
            f += 6
        return True
def prime_dividers (number):
    dividers = []
    n = 2
    while number > 1:
        if prime_factor(n):
            while number % n == 0:
                dividers.append(n)
                number /= n
        n += 1
    return dividers

dividers_of_smallest_number = []
for i in range (20,1,-1):
    div = prime_dividers(i)
    for l in div:
        if l in dividers_of_smallest_number:
            dividers_of_smallest_number.remove(l)
    dividers_of_smallest_number += div
smallest_number = 1
for i in dividers_of_smallest_number:
    smallest_number *= i
print(smallest_number)
print("Elapsed Time: ",(time.time() - start_time))