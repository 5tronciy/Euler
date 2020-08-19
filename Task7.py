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

prime_factors = []
i = 2
while len(prime_factors) < 10001:
    if prime_factor(i):
        prime_factors.append(i)
    i += 1
print(prime_factors[10000])
print("Elapsed Time: ",(time.time() - start_time))