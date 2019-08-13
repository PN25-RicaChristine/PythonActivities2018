from math import *
from tkinter import *

k = 0;
fileName = "calculator.txt"
WRITE = 'w'
READ = 'r'
APPEND = 'a'
file = open(fileName, mode = WRITE)
file.close()

file = open(fileName, mode = APPEND)
data = ("This is my Final Project for SD 101- a scientific calculator." + "\n" + "-" * 50)
file.write(data)
file.close()

error = "Syntax Error"

a = Tk(className = " Scientific Calculator-SD101")

display = Entry(a, bd = 5, bg = 'white', justify = "right")
display.grid(ipadx = 140, ipady = 8, columnspan = 10)



file = open(fileName, mode = APPEND)


def one():
    """Number 1"""
    display.insert(END, 1)
def two():
    """Number 2"""
    display.insert(END, 2)

def three():
    """Number 3"""
    display.insert(END, 3)

def four():
    """Number 4"""
    display.insert(END, 4)

def five():
    """Number 5"""
    display.insert(END, 5)

def six():
    """Number 6"""
    display.insert(END, 6)

def seven():
    """Number 7"""
    display.insert(END, 7)

def eight():
    """Number 8"""
    display.insert(END, 8)

def nine():
    """Number 3"""
    display.insert(END, 9)

def zero():
    """Number 0"""
    
    display.insert(END, 0)

def dec():
    """For decimal point"""
    display.insert(END, ".")


# for operators application


try:
    def add():
        """for addition"""
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " + ")

    def sub():
        """for subtraction"""
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " - ")

    def mul():
        """for multiplication"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " * ")

    def div():
        """for division"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " / ")

    def per() :
        """for percentage"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else :
            display.insert(END, " % ")


    def sign():
        """for sign and unsign"""
        display.insert(END, "-")
        
except ValueError:
    display.insert(error)


try:
    def eq():
        """for equations"""
        s = display.get()
        try :
            file = open(fileName, mode = APPEND)
            file.write("\n" + s)
            file.close()
        except UnicodeEncodeError :
            pass
        if (len(s) == 0):
            display.insert(END, "")
        elif (len(s) == 1): 
            display.delete(0, END)
            display.insert(END, s)
        else :
            s = display.get()
            s = s.split()
            if (s[1] == "+"):  
                try:
                    s = float(s[0]) + float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
            elif (s[1] == "-"):  
                try:
                    s = float(s[0]) - float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
            elif (s[1] == "*"):  
                try:
                    s = float(s[0]) * float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == "/"):  
                try:
                    s = float(s[0]) / float(s[2])
                    display.delete(0, END)
                    display.insert(0, str(s))
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ZeroDivisionError:
                    display.delete(0, END)
                    display.insert(0, "Cannot devide by zero")
            elif (s[1] == '%'):  
                try:
                    if (len(s) == 0):
                        display.insert(END, "")
                    else:
                        s = float(s[0]) / 100
                        display.delete(0, END)
                        display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)

            ################################################scientific calc###################
            elif (s[1] == '!') : #for factorial
                try:
                    s = str(factorial(int(s[0])))
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, "Give a positive integer!")

            elif (s[0] == '√') : #for underRoot
                try:
                    s = pow((float(s[1])), 1/2) #there is a problem of incoding
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, "Imaginary Number!")

            elif (s[0] == 'sin(') : #for sin
                try:
                    a = (int(s[1])) * pi / 180
                    s = sin(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'cos(') : #for cos
                try:
                    a = (int(s[1])) * pi / 180
                    s = cos(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'tan(') : #for cos
                try:
                    a = (int(s[1])) * pi / 180
                    s = tan(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'ln(') : #for ln
                try:
                    a = (float(s[1]))
                    s = log(a) #here base is e
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == 'log(') : #for log
                try:
                    a = (float(s[1]))
                    s = log(a, 10) #here base is e
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[0] == '1/'):   #for inverse
                try:
                    a = float(s[1])
                    s = 1/ a;
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)




            elif (s[0] == 'e^(') : #for exponential
                try:
                    a = (float(s[1]))
                    s = exp(a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)


            elif (s[1] == '^2') : #for exponential
                try:
                    a = (float(s[0]))
                    s = pow(a, 2)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == '^') : #for x raised to the power n..
                try:
                    a = (float(s[2]))
                    s = pow(float(s[0]),a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

            elif (s[1] == '^') : #for x raised to the power n..
                try:
                    a = (float(s[2]))
                    s = pow(float(s[0]),a)
                    display.delete(0, END)
                    display.insert(0, str(s))
                except IndexError:
                    display.delete(0, END)
                    display.insert(0, error)
                except ValueError:
                    display.delete(0, END)
                    display.insert(0, error)

           # elif (s[0] == 'pi'):   #for percentage
            #    try:
             #       s = pi
              #      display.delete(0, END)
               #     display.insert(0, str(s))
                #except IndexError:
                 #   display.delete(0, END)
                  #  display.insert(0, error)

            try:
                file = open(fileName, mode=APPEND)
                n = " = " + str(s) + '\n' + ('-' * 50)
                file.write(n)
                file.close()
            except UnicodeEncodeError:
                pass
except ValueError :
    display.delete(0, END)
    display.insert(0, error)
except IndexError:
    display.delete(0, END)
    display.insert(0, error)

# button for digits
onE = Button(a, text = '1', activebackground = 'Green',activeforeground = 'white'
             , bd = 8, bg = 'cyan'
             , command = one, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
onE.grid(row = 8, column = 0,pady=0,ipadx=17,ipady=10)

twO = Button(a, text = '2', activebackground = 'Green'
             , activeforeground = 'white', bd = 8, bg = 'cyan'
             , command = two, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
twO.grid(row = 8, column = 1,pady=0,ipadx=17,ipady=10)

threE = Button(a, text = '3', activebackground = 'Green'
               , activeforeground = 'white', bd = 8, bg = 'cyan'
               , command = three, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
threE.grid(row = 8, column = 2,pady=0,ipadx=17,ipady=10)

fouR = Button(a, text = '4', activebackground = 'Green'
              , activeforeground = 'white', bd = 8, bg = 'cyan'
              , command = four, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
fouR.grid(row = 7, column = 0,pady=0,ipadx=17,ipady=10)

fivE = Button(a, text = '5', activebackground = 'Green'
              , activeforeground = 'white', bd = 8, bg = 'cyan'
              , command = five, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
fivE.grid(row = 7, column = 1,pady=0,ipadx=17,ipady=10)

siX = Button(a, text = '6', activebackground = 'Green'
             , activeforeground = 'white', bd = 8, bg = 'cyan'
             , command = six, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
siX.grid(row = 7, column = 2,pady=0,ipadx=17,ipady=10)

seveN = Button(a, text = '7' , activebackground = 'Green'
               , activeforeground = 'white',  bd = 8, bg = 'cyan'
               , command = seven, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
seveN.grid(row = 6, column = 0,pady=0,ipadx=17,ipady=10)

eighT = Button(a, text = '8', activebackground = 'Green'
               , activeforeground = 'white', bd = 8, bg = 'cyan'
               , command = eight, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
eighT.grid(row = 6, column = 1,pady=0,ipadx=17,ipady=10)

ninE = Button(a, text = '9', activebackground = 'Green'
              , activeforeground = 'white', bd = 8, bg = 'cyan'
              , command = nine, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
ninE.grid(row = 6, column = 2,pady=0,ipadx=17,ipady=10)

zerO = Button(a,  text = '0', activebackground = 'Green'
              , activeforeground = 'white', bd = 8, bg = 'cyan'
              , command = zero, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
zerO.grid(row = 9, column = 0,pady=0,ipadx=16,ipady=10)

deC = Button(a, text = '.', activebackground = 'Green'
             , activeforeground = 'white', bd = 8, bg = 'cyan'
             , command = dec, fg = 'Indigo', justify = 'center', relief = 'groove'
             , state = "normal")
deC.grid(row = 9, column = 1,pady=0,padx=0,ipadx=17,ipady=10)

# this button for assigning the positive and negative value....
sigN = Button(a, text = '±', activebackground = 'Green'
              , activeforeground = 'white', bd = 8, bg = 'cyan'
              , command = sign, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
sigN.grid(row = 9, column = 2,pady=0,padx=0,ipadx=16,ipady=10)


## button for operators
# for % operator
peR = Button(a, text = ' % ', activebackground = 'Green'
              , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
              , command = per, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
peR.grid(row = 8, column = 4,pady=0,ipadx=14,ipady=10)
# button for +
plus = Button(a, text = '+', activebackground = 'Green'
              , activeforeground = 'white', bd = 8, bg = 'violet'
              , command = add, fg = 'Indigo', justify = 'center', relief = 'groove'
              , state = "normal")
plus.grid(row = 8, column = 3,pady=0,ipadx=14,ipady=10)

# button for -
minus = Button(a, text = '-', activebackground = 'Green'
               , activeforeground = 'white', bd =  8, bg = 'violet'
               , command = sub, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
minus.grid(row = 7, column = 3,pady=0,ipadx=15,ipady=10)

# button for *
multiply = Button(a, text = '*', activebackground = 'Green'
                  , activeforeground = 'white', bd = 8, bg = 'violet'
                  , command = mul, fg = 'Indigo', justify = 'center', relief = 'groove'
                  , state = "normal")
multiply.grid(row = 6, column = 3,pady=0,ipadx=15,ipady=10)

# button for /
divide = Button(a, text = '/', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'violet'
                , command = div, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
divide.grid(row = 5, column = 3,pady=0,ipadx=15,ipady=10)



# button for = 
equal = Button(a, text = '=', activebackground = 'green'
               , activeforeground = 'white', bd = 8, bg = 'yellow'
               , command = eq, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
equal.grid(row = 9, column = 3,pady=0,ipadx=14,ipady=10)



def clear():
    """for clear the screen"""
    display.delete(0, END)


reset = Button(a, text = 'C', activebackground = 'Green'
               , activeforeground = 'white', bd = 8, bg = 'lavender'
               , command = clear, fg = 'Indigo', justify = 'center', relief = 'groove'
               , state = "normal")
reset.grid(row = 5, column = 0,pady=0,ipadx=15,ipady=10)



def deleT():
    """delete a value"""
    display.delete((display.index(1000)) - 1)
    


deletE = Button(a, text = 'Del', activebackground = 'Green'
                , activeforeground = 'yellow', bd = 8, bg = 'pink'
                , command = deleT, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
deletE.grid(row = 5, column = 1,pady=0,ipadx=10,ipady=10)


try:
    def braces():
        """for braces"""
        s = display.get()
        s = s.split()
        if (len(s) == 2) :
            display.insert(END, " )")
        else :
            display.insert(END, "")


    def fact():
        """for factorial"""
        s = display.get()
        if (len(s) == 0) :
            display.insert(END, "")
        else :
            display.insert(END, " !")
  
    def underRoot():
        """ for Square Root"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "√ ")
        else :
            display.insert(END, "")
            
    def sine():
        """for sin"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "sin( ")
        else :
            display.insert(END, "")
            
    def cosine() :
        """for cos"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "cos( ")
        else :
            display.insert(END, "")

    def tangent():
        """for tan"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "tan( ")
        else:
            display.insert(END, "")

    def loge():
        "for logarithm"
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "log( ")
        else:
            display.insert(END, "")

    def lne():
        """for natural logarithm"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "ln( ")
        else:
            display.insert(END, "")


    def inverse():
        """for inverse"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            display.delete(0, END)
            display.insert(END, ("1/ %s" %s))

    def expo():
        """for exponent"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "e^( ")
        else:
            display.insert(END, "")

    def sq():
        """for square"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            display.insert(END, " ^2 ")
            
    def power():
        """for power"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            display.insert(END, (" ^ "))

    def Abs():
        """for absolute"""
        s = display.get()
        s = s.split()
        if (len(s) == 0):
            display.insert(END, "")
        else:
            v = abs(float(s[0]))
            display.delete(0, END)
            display.insert(END, str(v))#incase of mode we use simple

    def pii():
        """for pi"""
        s = display.get()
        if (len(s) == 0):
            display.insert(END, " 3.141592 ") #slution for symble
        else:
            display.insert(END, "")

    def exit():
        """f0r turning off the calculator"""
        a.destroy()


except ValueError:
    display.insert(error)




#for braces
braceS = Button(a, text = '( )', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = braces, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
braceS.grid(row = 5, column = 4,pady=0,ipadx=17,ipady=10)


#button for factorial
facT = Button(a, text = 'n!', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = fact, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
facT.grid(row = 5, column = 5,pady=0,ipadx=16,ipady=10)


#button for Squre Root
undeR = Button(a, text ='√', activebackground = 'Green' # alt + 251
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = underRoot, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
undeR.grid(row = 5, column = 6,pady=0,ipadx=16,ipady=10)


#for sin
sinE = Button(a, text = 'sin', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = sine, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
sinE.grid(row = 6, column = 4,pady=0,ipadx=15,ipady=10)

#for cos
cosinE = Button(a, text = 'cos', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = cosine, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
cosinE.grid(row = 6, column = 5,pady=0,ipadx=12,ipady=10)

#for tan
taN = Button(a, text = 'tan', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = tangent, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
taN.grid(row = 6, column = 6,pady=1,ipadx=12,ipady=10)

#for log
loG = Button(a, text = 'log', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = loge, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
loG.grid(row = 7, column = 4,pady=0,ipadx=14,ipady=10)

#for ln
lN = Button(a, text = 'ln', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = lne, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
lN.grid(row = 7, column = 5,pady=0,ipadx=16,ipady=10)

#for inverse
inveR = Button(a, text = '1/x', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = inverse, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
inveR.grid(row = 7, column = 6,pady=1,ipadx=12,ipady=10)

#for square
sQ = Button(a, text = ' x²', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = sq, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
sQ.grid(row = 8, column = 5,pady=1,ipadx=16,ipady=10)

#it's just give the x^n we can say...power
poweR = Button(a, text = ' xⁿ', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = power, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
poweR.grid(row = 8, column = 6,pady=0,ipadx=13,ipady=10)

#for absolute
abS = Button(a, text = '|x|', activebackground = 'Green'
                , activeforeground = 'white', bd = 9, bg = 'SpringGreen'
                , command = Abs, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
abS.grid(row = 9, column = 4,pady=1,ipadx=15,ipady=9)

#some constants
#for pi
pI = Button(a, text = 'π', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = pii, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
pI.grid(row = 9, column = 5,pady=0,ipadx=17,ipady=10)

#for exponent
exP = Button(a, text = 'eⁿ', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'SpringGreen'
                , command = expo, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
exP.grid(row = 9, column = 6,pady=0,ipadx=15,ipady=10)



#for closing the gui
exIT= Button(a, text = 'OFF', activebackground = 'Green'
                , activeforeground = 'white', bd = 8, bg = 'gray'
                , command = exit, fg = 'Indigo', justify = 'center', relief = 'groove'
                , state = "normal")
exIT.grid(row = 5, column = 2,pady=0,ipadx=9,ipady=10)

a.mainloop()

file = open(fileName, mode = APPEND)
file.write(("\n" + "Thanks buddy\n" + "-"*50))
file.close()
