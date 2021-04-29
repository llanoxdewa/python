def method(number1 = 1,number2 = 10,number3 = 20):
    for x in range(number1,number2+1):
        if(x < number3):
            continue
        print(x)
      


a = int(input('>> '))
b = int(input('>> '))
c = int(input('>> '))

method(a,b,c)


