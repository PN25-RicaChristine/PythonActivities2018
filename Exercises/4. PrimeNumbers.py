def prime(upper, lower):
   """This a program that displays prime numbers."""
   list1 = []
   for num in range(lower,upper):
       for i in range(2,num):
           if num%i == 0:
               break
       else:
           list1.append(num)
   return list1
up = int(input("upper: "))
low = int(input("lower: "))
print("Prime numbers between ",low," and ",up," is ",prime(up,low),".")


