import time
start_time = time.time()

def factors (number):
    k = 2
    for i in range (2, int(number/2+1)):
        if number % i == 0:
            k += 1
        i += 1
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
