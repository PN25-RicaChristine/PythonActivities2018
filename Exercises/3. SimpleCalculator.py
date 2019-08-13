print("Simple Calculator\n\n\nPress '+' if addition\nPress '-' if subtraction\nPress '*' if multiplication\nPress '/' if division\nPress '**' if square of a number\nPress '%' if you want to get remainder\n")
def cal(num1,oper,num2):
   if oper=="+":
     return (num1+num2)
   elif oper=="-":
     return num1-num2
   elif oper=="*":
     return num1*num2
   elif oper=="/":
     return num1/num2
   elif oper=="**":
     return num1**num2
   elif oper=="%":
     return num1%num2
print(cal(int(input("Num1: ")),str(input("Operation:")),int(input("Num2: "))))
