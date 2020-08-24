import time
start_time = time.time()

def next_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

def terms(first_number):
    k = 2
    while next_number(first_number) > 1:
        k += 1
        first_number = next_number(first_number)
    return k

limit = 1000000
longest_chain = 2
for i in range(limit):
    chain = terms(i)
    if chain > longest_chain:
        longest_chain = chain
        output = i

print(output, longest_chain)

print("Elapsed Time: ",(time.time() - start_time))
