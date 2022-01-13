class Bank:
    def __init__(self) -> None:
        pass

    # Reads text file into customer list
    def _load() -> None:
        pass

    # Return all customers in dict {Social Security Number: name}
    def get_customers() -> dict:
        pass

    # Creates a new customer, returns True if a customer was made
    def add_customer(name, ssn) -> bool:
        pass

    # Returns a list of customers information
    def get_customer(ssn) -> list:
        pass

    # Changes customer name if ssn exists in database
    def change_customer_name(name, ssn) -> bool:
        pass

    # Removes customer and returns that which was removed
    def remove_customer(ssn) -> list:
        pass

    # Adds an account to specified customer
    def add_account(ssn) -> str:
        pass

    # Returns a visual representation of all accounts belonging to customer
    def get_account(ssn, acc_id) -> str:
        pass

    # Deposits money into chosen account
    def deposit(ssn, acc_id, amount) -> bool:
        pass

    # Withdraws money into chosen account
    def withdraw(ssn, acc_id, amount) -> bool:
        pass

    # Closes active account and returns balance of closed account
    def close_account(ssn, acc_id) -> str:
        pass

    # Returns all transactions from account if it exists
    def get_all_transactions_by_ssn_acc_num(ssn, acc_num) -> str:
        pass
