number=13195
while(True):
    if(number%2==0):
        number=number/2
        print("divisible by 2")

    elif(number%3==0):
        number=number/3
        print("divisible by 3")

    elif(number%5==0):
        number=number/5
        print("divisible by 5")

    elif (number % 13 == 0):
        number = number / 13
        print("divisible by 13")

    elif (number % 29 == 0):
        number = number / 29
        print("divisible by 29")
    else:
        print("final value is",number)
        break
