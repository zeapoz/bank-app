from bank import *

bank = Bank()

def main():
    while True:
        print_instructions()
        choice = input().strip()
        match choice:
            case "1":
                add_customer()
            case "2":
                get_customer_info()
            case "3":
                add_account()
            case "4":
                deposit()
            case "5":
                withdraw()
            case "x":
                print("Quitting process...")
                break
            case _:
                print("Thats not a valid choice!")
                pass

def add_customer():
    name = input("Name for new customer: ").strip()
    ssn = input("Social security number for new customer: ").strip()
    bank.add_customer(name, ssn)

def get_customer_info():
    ssn = input("Enter their social security number: ").strip()
    print(bank.get_customer_info(ssn))

def add_account():
    ssn = input("Enter customers social security number: ").strip()
    acc_type = input("Enter type of account (debit account): ").strip()
    acc_num = input("Enter card number: ").strip()
    account = Account(acc_type, acc_num)
    bank.add_account(ssn, account)

def deposit():
    ssn = input("Enter customers social security number: ").strip()
    acc_id = input("Enter customers account number: ").strip()
    amount = float(input("Enter deposit amount: ").strip())
    bank.deposit(ssn, acc_id, amount)

def withdraw():
    ssn = input("Enter customers social security number: ").strip()
    acc_id = input("Enter customers account number: ").strip()
    amount = float(input("Enter withdrawal amount: ").strip())
    bank.withdraw(ssn, acc_id, amount)

def print_instructions():
    print("\nWhat do you want to do? (Enter corresponding number)")
    print("1: Add a new customer")
    print("2: Get info about a customer")
    print("3: Add a new account to existing customer")
    print("4: Deposit money to existing customers account")
    print("5: Withdraw money from existing customers account")
    print("x: Quit program")
    print("-" * 36)

if __name__ == "__main__":
    main()
