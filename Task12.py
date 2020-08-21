import time
start_time = time.time()

def is_square (number):
    sq = number**0.5
    if sq - round(sq) == 0:
        return True

def factors (number):
    k = 2
    for i in range (2, int(number**0.5)):
        if number % i == 0:
            k += 2
        i += 1
    if is_square(number):
        return k - 1
    else:
        return k

n = 1
limit = 500
l = 2
while l < limit:
    m = n*(n+1)/2
    l = factors(m)
    print(n, m, l)
    n += 1

print("Elapsed Time: ",(time.time() - start_time))
