"""This a function for calculator"""

def add(a,b):
    """This function adds number."""
    return "The sum of "+str(a)+" and "+str(b)+": "+str(a+b)

def sub(a,b):
    """This function subtracts number."""
    return "The difference between "+str(a)+" and "+str(b)+": "+str(a-b)

def mul(a,b):
    """This function multiplies number."""
    return "The product of "+str(a)+" and "+str(b)+": "+str(a*b)

def div(a,b):
    """This function divides number."""
    return "The qoutient of "+str(a)+" divided by "+str(b)+": "+str(a/b)

def fact(a):
    """This function shows the factorial of a number."""
    factorial=1
    if a < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif a == 0:
        return "The factorial of 0 is 1"
    else:
        for i in range(1,a + 1):
            factorial = factorial*i
        return "The factorial of "+str(a)+": "+str(factorial)
    
def pow(a,b):
    """This functions show the result of a number to the power of a number."""
    return str(a)+" to the power of "+str(b)+": "+str(a**b)

def dec_to_bin(a):
    """This functions converts decimal to binary."""
    b=""
    while a!=0:
        if a%2==0:
            a=(a/2)
            b=b+"0"
        else:
            a=(a-1)/2
            b=b+"1"
    return "Decimal to binary :"+str(b[::-1])

def mod(a,b):
    """This function shows the remainder with the use of modulo"""
    return "Using modulo the remainder of "+str(a)+" divided by "+str(b)+": "+str(a%b)

def floored(a,b):
    """This function shows the floored division of a certain number"""
    return "The floored qoutient of "+str(a)+" divided by "+str(b)+": "+str(a//b)

def sqrt(a):
    """This function shows the square root of a number."""
    return "The square root of "+str(a)+": "+str(a**0.5)
