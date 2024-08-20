def gcd(num1, num2):
    if num1 ==0 and num2 == 0:
        return 'Error! must be not all zero.'
    elif num2 == 0:
        return num1
    return gcd(num2,num1%num2)
num1, num2 = [int(x) for x in input('Enter Input : ').split()]
maximum = max(num1, num2)
minimum = min(num1,num2)
gcd = gcd(num1, num2)
print(f'The gcd of {maximum} and {minimum} is : {abs(gcd)}' if isinstance(gcd, int) else gcd) 