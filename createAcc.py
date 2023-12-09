class BankAccount:
    def __init__(self, account_name, initial_deposit, account_type):
        self.account_name = account_name
        self.account_type = account_type
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount}$ has been deposited, current balance is {self.balance}$.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Amount {amount}$ has been withdrawn, current balance is {self.balance}$.")

    def display_balance(self):
        print(f"Account Name: {self.account_name}, Account Type: {self.account_type}, Current Balance: {self.balance}$.")

def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter the initial deposit amount: $"))
    account_type = input("Enter the account type (Savings/Current): ")
    new_account = BankAccount(name, initial_deposit, account_type)
    new_account.display_balance()
    return new_account

def menu():
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Exit")

account = None
while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        account = create_account()
    elif choice == 2:
        if account is not None:
            amount = float(input("Enter the amount to deposit: $"))
            account.deposit(amount)
        else:
            print("Please create an account first.")
    elif choice == 3:
        if account is not None:
            amount = float(input("Enter the amount to withdraw: $"))
            account.withdraw(amount)
        else:
            print("Please create an account first.")
    elif choice == 4:
        if account is not None:
            account.display_balance()
        else:
            print("Please create an account first.")
    elif choice == 5:
        break
    else:
        print("Invalid choice, please choose a valid option.")