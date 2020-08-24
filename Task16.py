import time
start_time = time.time()
sum = 0
for i in str(2**1000):
    sum += int(i)
print(sum)

print("Elapsed Time: ",(time.time() - start_time))
