from bank import *

bank = Bank()

def main():
    while True:
        # Temporary save on change
        bank.write_to_file("./data.txt")
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
            case "6":
                close_account()
            case "7":
                remove_customer()
            case "8":
                get_all_transactions()
            case "x":
                print("Saving changes...")
                bank.write_to_file("./data.txt")
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
    # acc_type = input("Enter type of account (debit account): ").strip()
    bank.add_account(ssn)

def get_customer_accounts(ssn):
    # Returns customers account in human-readable format
    cus = bank.get_customer(ssn)
    acc_enum = list(enumerate(cus.accounts, 1))
    for i, acc in acc_enum:
        print(f"{i}: Account #{i}, balance: {acc.balance}")
    choice = int(input("Choose an account: "))
    if choice < 1 or choice > len(acc_enum):
        print_error("Error: Not a valid choice.")
        return False
    _, acc = acc_enum[choice - 1]
    return acc.acc_id

def deposit():
    ssn = input("Enter customers social security number: ").strip()
    acc_id = get_customer_accounts(ssn)
    if acc_id:
        amount = float(input("Enter deposit amount: ").strip())
        bank.deposit(ssn, acc_id, amount)

def withdraw():
    ssn = input("Enter customers social security number: ").strip()
    acc_id = get_customer_accounts(ssn)
    if acc_id:
        amount = float(input("Enter withdrawal amount: ").strip())
        bank.withdraw(ssn, acc_id, amount)

def close_account():
    ssn = input("Enter customers social security number: ").strip()
    acc_id = input("Enter customers account number: ").strip()
    print(f"The closed account had {bank.close_account(ssn, acc_id)}")

def remove_customer():
    ssn = input("Enter customers social security number: ").strip()
    bank.remove_customer(ssn)

def get_all_transactions():
    for trans in bank.transactions:
        print(trans)

def print_instructions():
    print("\nWhat do you want to do? (Enter corresponding number)")
    print("1: Add a new customer")
    print("2: Get info about a customer")
    print("3: Add a new account to existing customer")
    print("4: Deposit money to existing customers account")
    print("5: Withdraw money from existing customers account")
    print("6: Close customers account")
    print("7: Remove customer")
    print("8: View all transactions")
    print("x: Quit program")
    print("-" * 36)

if __name__ == "__main__":
    main()
