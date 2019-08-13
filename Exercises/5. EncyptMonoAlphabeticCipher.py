def encrypt(a=input("Text: ")):
 """this is a program that encrypt texts."""
 alpha_lower="abcdefghijklmnopqrstuvwxyz"
 alpha_upper="abcdefghijklmnopqrstuvwxyz".upper()
 key=int(input("Key: "))
 c=0
 cipher=""
 for i in a:
   if i.islower()==True:
     c=key+alpha_lower.index(i)
     cipher+=alpha_lower[c%26]
   elif i.isalpha()==False:
     continue
   else:
     c=key+alpha_upper.index(i)
     cipher+=alpha_upper[c%26]
 return cipher
print("Ciphertext:",encrypt())
