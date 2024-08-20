def factorial(number:int)->int:
    if(number == 0):
        return 1
    return number * factorial(number-1)

number = input('Enter Number : ')
print(f'{number}! = {factorial(int(number))}')
