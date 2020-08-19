#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import time
start_time = time.time()
def palindromic(number):
    if str(number) == str(number) [::-1]:
        return 'палиндром'

largest_palindromic = 0
for k in range (999, 1, -1):
    for l in range (999, 1, -1):
        if palindromic(k * l) == 'палиндром' and k * l > largest_palindromic:
            largest_palindromic = k * l
print(largest_palindromic)
print("Elapsed Time: ",(time.time() - start_time))