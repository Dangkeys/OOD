print('*** multiplication or sum ***')
num1, num2 = [int(x) for x in input('Enter num1 num2 : ').split()]
print('The result is ',end='')
if(num1 * num2 > 1000):
    print(num1 + num2)
else:
    print(num1 * num2)