import time
start_time = time.time()
fibonacchi = [1, 2]
sum = 2
while fibonacchi[-1] < 4000000:
    fibonacchi.append(fibonacchi[-1]+fibonacchi[-2])
    if fibonacchi[-1] % 2 == 0 and fibonacchi[-1] < 4000000:
        sum += fibonacchi[-1]
print(sum)
print("Elapsed Time: ",(time.time() - start_time))