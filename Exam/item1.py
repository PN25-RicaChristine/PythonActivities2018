def function1(*args):
    """This function  accepts a string and returns a char frequency list but if 2 arguments are passed, function1
accepts a string and a character and the function checks if the said character is in the string and
enumerates how many times it appeared."""
    lst=[]
    if len(args)==1:
        for i in args[0]:
            if i not in lst:
                lst.extend([i,args[0].count(i)])
        return lst
    elif len(args)==2:
        if args[1] in args[0]:
            lst.extend([args[1],args[0].count(args[1])])
            return lst
        else:
            return False
print(function1("google.com"))
print(function1("test","t"))
print(function1("test", "T"))

def function2(string):
    """This function t accepts a string and returns the most
frequent character in the string but if 2 characters share the same frequency, display the character with
the most significant value in the english alphabet."""
    a=[]
    b=[]
    c=[]
    s=[]
    for i in string:
        a.append(string.count(i))
    for i in range(len(a)):
        if a[i]==max(a):
            b.append(string[i])
    for j in b:
        if j==" ":
            continue
        s.append(j)
    return min(s)
print(function2("characater"))
print(function2("this is a test"))
