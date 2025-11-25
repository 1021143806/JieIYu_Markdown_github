print('Hello')
print('World')
import random
for x in range(0,10):
    randomNumber1 = random.randint(1,6)
    randomNumber2 = random.randint(1,6)
    total = randomNumber1 + randomNumber2
    print(total)
    #首先判断两个数是不是一样
    if randomNumber1 == randomNumber2:
        print("double")
    else:
        #如果不一样，判断两数之和读到大小
        if total >  8:
            print("big")
        elif total >4 and total <=8:
            print ("not bad")
        else:
            print("small")
            