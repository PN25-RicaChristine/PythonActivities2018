def accnum():
    """This is for the account number"""
    global Acc
    global fund
    global enter
    Acc={'18106123':'1234','18106234':'2345','18106345':'3456','18106456':'4567','18106567':'5678'}
    fund={'18106123':10000,'18106234':10000,'18106345':10000,'18106456':10000,'18106567':10000}
    print("\nWelcome to ATM Machine\n")
    enter=input("Enter account number: ")
    if enter not in Acc:
        print("ACCOUNT NUMBER DOES NOT EXIST.")
        accnum()
    else:
        pins()
def pins():
    """This is for the account pins"""
    chance=0
    while 1:
        accpin=input("Enter PIN: ")
        if accpin != Acc[enter]:
            print("PIN DOES NOT MATCHES THE ACCOUNT NUMBER.Try again!")
            chance+=1
        else:
            displaymenu()
        if chance == 3:
            accnum()
            break
def displaymenu():
    """This is for the display menu to select transaction"""
    print( "\nSelect Transaction\nPress 1 for Balance Inquiry\nPress 2 for Withdrawal\nPress 3 for Deposit\nPress 0 to Exit")
    choice()
def inquiry():
    """This is for balance inquiry"""
    print( "CURRENT BALANCE : ",fund[enter])
    displaymenu()
    choice()
def withdraw():
    """This is for withdrawal transaction"""
    wid=int(input("Amount withdraw: "))
    if wid>fund[enter]:
        print("FUND IS NOT ENOUGH")
        print("CURRENT BALANCE :", fund[enter])
        choice()  
    else:
        fund[enter]-=wid
        print("CURRENT BALANCE :",fund[enter])
        displaymenu()
        choice()
def deposit():
    """This is for deposit transaction"""
    dep=int(input(("\nAmount to deposit: ")))
    fund[enter]+=dep
    print("TOTAL CASH ON BANK :",fund[enter])
    displaymenu()
    choice()
def choice():
    """This is for the selected transaction"""
    select=int(input("\nEnter Transaction: "))
    if select==1:
        inquiry()
    if select==2:
        withdraw()
    if select==3:
        deposit()
    if select==0:
        print("\nThank You For Banking!!!\nHave a nice day!!")
        exit()

accnum()
