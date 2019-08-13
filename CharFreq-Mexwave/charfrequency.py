def function_1(*args):
    """This functions accepts a string and returns a char frequency list. If 2 arguments is passed, it accepts a string and a character and the function checks if the said character is in the string and enumerates how many times it appeared.  """
    if len(args)==1:
        arg1=[]
        for i in args[0]:
            if i not in arg1:
                arg1.extend([i,args[0].count(i)])
        return arg1
    elif len(args)==2:
        if args[1] in args[0]:
            return "True",args[0].count(args[1])
        else:
            return "False",args[1]

def function_2(argu):
    """This function accepts a string and returns the most frequent character in the string. If 2 characters share the same frequency, display the character with the most significant value in the english alphabet. 
"""
    arg=argu.lower()
    a=[]
    b=[]
    for i in arg:
        a.append(arg.count(i))
    for i in range(len(a)):
        if a[i] ==  max(a):
            b.append(arg[i])
    return "Output: "+str(min(b))
