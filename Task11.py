import time
start_time = time.time()

with open("11_input.txt", "r") as file:
    contents = file.readlines()
massiv = []

for i in range(20):
    m = contents[i].split(' ')
    massiv.append(m)

greatest_product = 1
for j in range(20):
    for i in range(20):
        # Проверка в ряду
        if i < 17:
            product = int(massiv [j][i])*int(massiv[j][i+1])*int(massiv[j][i+2])*int(massiv[j][i+3])
            if product > greatest_product:
                greatest_product = product
                ind = [j, i, 'ряд']
        # Проверка в столбце
        if j < 17:
            product = int(massiv[j][i]) * int(massiv[j+1][i]) * int(massiv[j+2][i]) * int(massiv[j+3][i])
            if product > greatest_product:
                greatest_product = product
                ind = [j, i, 'столбец']
        # Проверка диагонали слева направо
        if i < 17 and j < 17:
            product = int(massiv[j][i]) * int(massiv[j+1][i+1]) * int(massiv[j+2][i+2]) * int(massiv[j+3][i+3])
            if product > greatest_product:
                greatest_product = product
                ind = [j, i, 'диагональ направо']
        # Проверка диагонали справа налево
        if i > 2 and j < 17:
            product = int(massiv[j][i]) * int(massiv[j+1][i-1]) * int(massiv[j+2][i-2]) * int(massiv[j+3][i-3])
            if product > greatest_product:
                greatest_product = product
                ind = [j, i, 'диагональ налево']

print(greatest_product)
print(ind)
print("Elapsed Time: ",(time.time() - start_time))