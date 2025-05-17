a=int(input('Enter a number:'))
def factorial(x):
    if x<2:
        return 1
    else:
        fac=x*(factorial(x-1))
        return fac
z=factorial(a)
print('Factorial of',a,'is:',z)