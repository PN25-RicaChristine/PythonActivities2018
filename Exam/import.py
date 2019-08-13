import item1
import item2
import memereview

print("Number 1 item:\n")
print(item1.function1("google.com"))
print(item1.function1("test","t"))
print(item1.function1("test", "T"))
print(item1.function2("characater"))
print(item1.function2("this is a test"))


print("\n\nNumber 2 item:\n")
print(item2.palindrome("raceCar"))
print(item2.palindrome("RACEcar"))
print(item2.palindrome("test"))
print(item2.construct("facecheck","chafe") )
print(item2.construct("facecheck", "chaFe"))
print(item2.construct("fibonacci","cincaa"))

print("\n\nNumber 3 item:\n")
print(memereview.skrattadu("aaabb",3))
print(memereview.skrattadu("abb",3))
print(memereview.forloradu(23,48))
print(memereview.forloradu(48,23))
print(memereview.MrBeastSama(True))
print(memereview.MrBeastSama(False))
