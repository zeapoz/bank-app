from customer import *
from account import *

class Bank:
    def __init__(self) -> None:
        print("Welcome to the bank application!")
        self.customers = self._load("./data.txt")

    # Reads text file into customer list
    def _load(self, path) -> list:
        customers = []
        # Open and read file
        file = open(path)
        lines = file.readlines()
        for line in lines:
            # Create customer
            data = line.split(":")
            id = data[0]
            name = data[1]
            ssn = data[2]
            customer = Customer(id, name, ssn)
            customers.append(customer)
            # Credit information
            # TODO Accept multiple accounts
            acc_num = data[3]
            acc_type = data[4]
            acc_balance = data[5]
            customer.add_account(Account(acc_type, acc_num, acc_balance))
            # Set increments
            self.cus_id_increment = int(id) + 1
            self.acc_num_increment = int(acc_num) + 1
        file.close()
        return customers

    # Return all customers in dict {Social Security Number: name}
    def get_customers(self) -> dict:
        customers = {}
        for c in self.customers:
            customers[c.ssn] = c.name, c
        return customers

    # Creates a new customer, returns True if a customer was made
    def add_customer(self, name, ssn) -> bool:
        customer = Customer(self.cus_id_increment, name, ssn)
        self.cus_id_increment += 1
        self.customers.append(customer)

    def get_customer(self, ssn) -> Customer:
        customer = self.get_customers().get(ssn)
        if customer:
            customer = customer[1]
            return customer
        print("Error customer not found!")
        return -1

    # Returns a list of customers information
    def get_customer_info(self, ssn) -> list:
        # Find customer
        # customer: Customer = None
        customer = self.get_customer(ssn)
        if customer:
            # TODO Customer account info getter
            info = [customer.name, customer.ssn, customer.id, customer.accounts]
            return info

    # Changes customer name if ssn exists in database
    def change_customer_name(name, ssn) -> bool:
        pass

    # Removes customer and returns that which was removed
    def remove_customer(ssn) -> list:
        pass

    # Adds an account to specified customer
    def add_account(self, ssn, account) -> str:
        customer = self.get_customer(ssn)
        if customer:
            if customer.add_account(account):
                print(f"Successfully added new account to {customer.name}")
            else:
                print(f"Error: Could not add new account to {customer.name}")

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
