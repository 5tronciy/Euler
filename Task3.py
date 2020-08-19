#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
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

#big_number = 600851475143
#primes = []
#j = 2
#while j < big_number:
#    if prime_factor(j) == 'простое число':
#        primes.append(j)
#    j += 1
#primes.reverse()
#print(primes)

#for prime in primes:
#   if big_number % prime == 0:
#        print(prime)
#        break

number = 600851475143
n = 2
while number > 1:
    if prime_factor(n):
        while number % n == 0:
            number /= n
    n += 1
print(n-1)
print("Elapsed Time: ",(time.time() - start_time))