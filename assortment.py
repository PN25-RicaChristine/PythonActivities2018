def function_1(a,b,c):
    """This function finds the max among three numbers."""
    d=[a,b,c]
    return "Maximum num: "+str(max(d))


def function_2(string):
    """This function accepts a string, reverses it and returns a list containing the reversed string, and the most frequent character. If there are 2 or more characters with the same amount of frequency, return the one that occured with the most frequency first."""
    a = string.lower()
    lst=[a[::-1]]
    b = a[0]
    for i in range(1,len(a)):
        if a.count(b) < a.count(a[i]):
            b = a[i]
        if a.count(b) == a.count(a[i]):
            d = 0
            e = 0
            for j in a:
                if j == b:
                    d += 1
                    if d == a.count(b):
                        b = b
                        break
                elif j == a[i]:
                    e += 1
                    if e == a.count(a[i]):
                        b = a[i]
                        break
    lst.append(b)
    return "Output: "+str(lst)

def function_3(*args):
    """This function accepts any number of words as input, and returns the words reversed and with the first letters capitalized.
"""
    lst=[]
    for k in args:
        i=k.lower()
        j=i[0].upper()+i[1:]
        lst.append(j[::-1])
    return "Output: "+str(lst)

