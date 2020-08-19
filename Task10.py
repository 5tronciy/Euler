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
        r = math.floor(n ** 0.5)
        f = 5
        while f <= r:
            if number % f == 0:
                return False
            if number % (f+2) == 0:
                return False
            f += 6
        return True

limit = 2000000
sum = 5
n = 5
while n <= limit:
    if prime_factor(n):
        sum += n
    n += 2
    if n <= limit and prime_factor(n):
        sum += n
    n += 4
#    print(n)

#for i in range(2,2000001):
#    if prime_factor(i):
#        sum += i
#        print(i)
print(sum)
print("Elapsed Time: ",(time.time() - start_time))