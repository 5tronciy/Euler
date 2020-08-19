import time
start_time = time.time()
number = 1000
summa = 0
for i in range(1, number):
    if i % 3 == 0 or i % 5 == 0:
        summa += i
        i += 1
print(summa)
print("Elapsed Time: ",(time.time() - start_time))