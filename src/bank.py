import os
import colorama

from customer import *
from account import *

class Bank:
    def __init__(self) -> None:
        welcome_s = "| Welcome to the bank application! |"
        print("-" * len(welcome_s))
        print(welcome_s)
        print("-" * len(welcome_s))
        self.customers = self._load("./data.txt")

    # Reads text file into customer list
    def _load(self, path) -> list:
        # Check if file exists
        if not os.path.exists(path):
            self.print_error("Error: No database file found in \"./data.txt\"")
            self.print_error("Changes made will be written to a new file at the path.")
            return
        customers = []
        # Open and read file
        file = open(path)
        lines = file.readlines()
        for line in lines:
            # Seperate customer and acccounts
            data = line.split("#")
            # Create customer
            cus_data = data[0].split(":")
            id = cus_data[0]
            name = cus_data[1]
            ssn = cus_data[2]
            customer = Customer(id, name, ssn)
            customers.append(customer)
            # Credit information
            for i in range(len(data[1:])):
                acc_data = data[i].split(":")
                acc_num = acc_data[0]
                acc_type = acc_data[1]
                acc_balance = acc_data[2]
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
        if not self.get_customer(ssn, False):
            customer = Customer(self.cus_id_increment, name, ssn)
            self.cus_id_increment += 1
            self.customers.append(customer)
            self.print_success("New customer successfully added.")
            return True
        self.print_error("Error: Social security number already exists.")
        return False

    def get_customer(self, ssn, warn=True) -> Customer:
        customer = self.get_customers().get(ssn)
        if customer:
            customer = customer[1]
            return customer
        if warn:
            self.print_error("Warning: No customer with that social security number.")
        return None

    # Returns a list of customers information
    def get_customer_info(self, ssn) -> list:
        # Find customer
        customer = self.get_customer(ssn)
        if customer:
            # TODO Customer account info getter
            info = [customer.name, customer.ssn, customer.id, customer.accounts]
            return info

    # Changes customer name if ssn exists in database
    def change_customer_name(self, name, ssn) -> bool:
        customer = self.get_customer(ssn)
        if customer:
            customer.set_name(name)
            return True
        return False

    # Removes customer and returns that which was removed
    def remove_customer(ssn) -> list:
        pass

    # Adds an account to specified customer
    def add_account(self, ssn, account) -> str:
        customer = self.get_customer(ssn)
        if customer:
            if customer.add_account(account):
                self.print_success(f"Successfully added new account to {customer.name}")
            else:
                self.print_error(f"Could not add new account to {customer.name}")

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

    # Helper functions to print colored text
    def print_error(self, s):
        print(f"{colorama.Fore.RED}{s}{colorama.Style.RESET_ALL}")
    
    def print_success(self, s):
        print(f"{colorama.Fore.GREEN}{s}{colorama.Style.RESET_ALL}")
