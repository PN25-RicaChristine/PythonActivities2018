def skrattadu(username,number):
    """This function is for skrattadu. """
    for i in username:
        a=username.count(i)
        if a==number:
            return True
            break
        return False
print(skrattadu("aaabb",3))
print(skrattadu("abb",3))


def forloradu(first,second):
    """This function is for forloradu"""
    if first>second:
        return "Pewdiepie is winning!"
    return "Unsubscribe to T-Series!"
print(forloradu(3,8))
print(forloradu(8,3))


def MrBeastSama(boolean):
    """This fucntion is for MrBeastSama """
    if boolean==True:
        return "Brofist!"
    return "Bihk Lasagna"
print(MrBeastSama(True))
print(MrBeastSama(False))
