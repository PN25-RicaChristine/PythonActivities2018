def palindrome(string):
    """This function is for palindrome"""
    a=string.lower()
    if a==a[::-1]:
        return True
    return False
print(palindrome("raceCar"))
print(palindrome("RACEcar"))
print(palindrome("test"))

def construct(first,second):
    """This function is for construct"""
    c=0
    for i in second:
        j=second.count(i)
        if j<=first.count(i):
            c+=1
    if c==len(second):
        return True
    return False
    
print(construct("facecheck","chafe") )
print(construct("facecheck", "chaFe"))
print(construct("fibonacci","cincaa"))

    
            
    
