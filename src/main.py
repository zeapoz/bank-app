from bank import *

bank = Bank()

def main():
    while True:
        # Temporary save on change
        bank.write_to_file()
        print_instructions()
        choice = input().strip()
        match choice:
            # Customer
            case "1":
                get_customer_info()
            case "2":
                add_customer()
            case "3":
                remove_customer()
            case "4":
                change_customers_name()
            case "5":
                get_all_customers()
            # Account
            case "6":
                deposit()
            case "7":
                withdraw()
            case "8":
                add_account()
            case "9":
                close_account()
            # Transaction
            case "10":
                get_transactions_from_account()
            case "11":
                get_all_transactions()
            case "x":
                print("Saving changes...")
                bank.write_to_file()
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
    info = bank.get_customer_info(ssn)
    print(f"Name: {info[0]}, SSN: {info[1]}")
    get_customer_accounts(ssn, True)

def add_account():
    ssn = input("Enter customers social security number: ").strip()
    # acc_type = input("Enter type of account (debit account): ").strip()
    bank.add_account(ssn)

def get_customer_accounts(ssn, only_print=False):
    # Returns customers account in human-readable format
    cus = bank.get_customer(ssn)
    acc_enum = list(enumerate(cus.accounts, 1))
    if len(acc_enum) <= 0:
        print_error("Customer has no accounts.")
        return
    # Iterate through enumerized list to get index and account
    for i, acc in acc_enum:
        print(f"{i}: {acc.acc_type.capitalize()} #{i}, balance: {acc.balance}")
    if only_print:
        return
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
    acc_id = get_customer_accounts(ssn)
    if acc_id:
        print(f"The closed account had {bank.close_account(ssn, acc_id)} funds.")

def remove_customer():
    ssn = input("Enter customers social security number: ").strip()
    bank.remove_customer(ssn)

def get_all_transactions():
    for trans in bank.transactions:
        print(trans)

def get_all_customers():
    customers = bank.get_customers()
    print("\nSSN, Name")
    for c in customers.keys():
        print(f"{c}, {customers[c][0]}")
    
def change_customers_name():
    ssn = input("Enter customers social security number: ").strip()
    new_name = input("Enter customers new name: ")
    if bank.change_customer_name(new_name, ssn):
        print_success(f"Name was successfully changed to {new_name}")

def get_transactions_from_account():
    ssn = input("Enter customers social security number: ").strip()
    acc_id = get_customer_accounts(ssn)
    if not acc_id:
        return
    transactions = bank.get_all_transactions_by_ssn_acc_id(ssn, acc_id)
    for t in transactions:
        print(t)

def print_instructions():
    print("\n" + "-" * 36)
    print_accent("What do you want to do? (Enter corresponding number)")
    print_accent("Customer operations:")
    print("1: Get info about a customer")
    print("2: Add a new customer")
    print("3: Remove customer")
    print("4: Change customers name")
    print("5: Show list of all customers")
    print_accent("Account operations:")
    print("6: Deposit money to existing customers account")
    print("7: Withdraw money from existing customers account")
    print("8: Add a new account to existing customer")
    print("9: Close customers account")
    print_accent("Transaction info operations:")
    print("10: View all transaction from account")
    print("11: View all transactions")
    print_accent("Other:")
    print("x: Quit program")
    print("-" * 36)

if __name__ == "__main__":
    main()
