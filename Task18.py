import time
start_time = time.time()
with open("18_input.txt", "r") as file:
    contents = file.readlines()
massiv = []
for i in range(15):
    m = contents[i].split(' ')
    massiv.append(m)
i = 0
sum = int(massiv[0][0])
for j in range(1,15):
    if massiv[j][i] < massiv[j][i+1]:
        i += 1
    sum += int(massiv[j][i])
    print(massiv[j][i])
print(sum)
print("Elapsed Time: ",(time.time() - start_time))
