def function1(arg):
    """This functions accepts a string and returns a list containing a mexican wave for the string. """
    a=arg.lower()
    mex=[]
    for i in range(len(arg)):
        b=a[:i]+a[i].upper()+a[i+1:]
        mex.append(b)
    return mex


def function2(arg2):
    """This functions accepts a string and creates a recurring wave (e.g [Low, lOw, loW, Wol, wOl, woL])
"""
    a=arg2.lower()
    mex=[]
    for i in range(len(arg2)):
        b=a[:i]+a[i].upper()+a[i+1:]
        mex.append(b)
    for i in mex[::-1]:
        mex.append(i[::-1])
    return mex

