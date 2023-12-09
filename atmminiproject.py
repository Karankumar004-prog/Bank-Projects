balance=10000
pin=1234

while True:
    print('\n')
    print('Welcome to Bank'.center(90))
    print('*'*100)
    print('Menu Options')
    print('1.Check balance'.center(90))
    print("2.Withdrawal".center(90))
    print("3.Deposit".center(90))
    print("4.Change Pin".center(90))
    print("5.Exit".center(90))
    print("*"*100)
   
    n=input("Enter your choice:")
   
    if n=="1":
        k=int(input("Enter pin:"))
        if pin==k:
            print("\nYour Balance",balance)
        else:
            print("Invalid pin")
    elif n=="2":
        k=int(input("Enter pin:"))
        if pin==k:
            withdraw=int(input("Enter amount to withdraw:"))
            if balance >=withdraw:
                balance-=withdraw
                print("\n Withdrawal Sucessfull")
                print("New Balance:Rs ",balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid pin")
    elif n=="3":
        k=int(input("Enter pin:"))
        if pin==k:
            deposit=int(input("Enter amount to Deposit:"))
            balance+=deposit
            print("\nDeposit Sucessfull")
            print("Total Balance:Rs ",balance)
        else:
            print("Invalid pin")
    elif n=="4":
         k=int(input("Enter old pin:"))
         if pin==k:
             change=int(input("Enter new pin:"))
             pin=change
             print("Pin changed Successfully")
         else:
             print("Incorrect pin, Try Again")
    else:
        print("Thank you for visiting")
        break