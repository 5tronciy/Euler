import time
start_time = time.time()

dict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
        12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
        19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
        80:'eighty',90:'ninety'}

def literal(number):
    s=''
    if number > 99:
        if number == 1000:
            s = 'onethousand'
        elif number % 100 == 0:
            s = (dict[int(str(number)[0])] + 'hundred')
        else:
            s = (dict[int(str(number)[0])] + 'hundredand')
            if number % 100 in dict:
                s += dict[number % 100]
            else:
                if str(number)[1] == 0:
                    s += dict[int(str(number)[2])]
                else:
                    s += dict[number % 100 // 10 * 10] + dict[int(str(number)[2])]
    else:
        if number in dict:
            s += dict[number]
        else:
            if str(number)[0] == 0:
                s += dict[int(str(number)[1])]
            else:
                s += dict[number // 10 * 10] + dict[int(str(number)[1])]
    return s

sum = 0
for i in range(1,1001):
    sum += len(literal(i))
print(sum)
print("Elapsed Time: ",(time.time() - start_time))
