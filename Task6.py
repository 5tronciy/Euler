import time
start_time = time.time()
sum1 = 0
sum2 = 0
for i in range(1,101):
    sum1 += i ** 2
    sum2 += i
print(sum2 **2 - sum1)
print("Elapsed Time: ",(time.time() - start_time))