import os
from pickletools import read_string1
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
            # Account information
            for i in range(1, len(data)):
                acc_data = data[i].split(":")
                acc_id = acc_data[0]
                acc_type = acc_data[1]
                acc_balance = float(acc_data[2])
                customer.add_account(Account(acc_type, acc_id, acc_balance))
                # Set increments
                self.cus_id_increment = int(id) + 1
                self.acc_id_increment = int(acc_id) + 1
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

    # Fetches customer based on social security number, optional flag to warn if not found
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
        customer = self.get_customer(ssn)
        if customer:
            accounts = [(x.acc_id, x.balance) for x in customer.accounts]
            info = [customer.name, customer.ssn, accounts]
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

    # Returns account belonging to customer
    def get_account(self, customer, acc_id) -> Account:
        for acc in customer.accounts:
            if acc.acc_id == acc_id:
                return acc
        self.print_error("Error: Account id not matching customers.")
        return None

    # Deposits money into chosen account
    def deposit(self, ssn, acc_id, amount) -> bool:
        customer = self.get_customer(ssn)
        if not customer:
            return
        acc = self.get_account(customer, acc_id)
        print(acc)
        if acc:
            acc.deposit(amount)
            self.print_success(f"{amount} successfully deposited into account id {acc_id} belonging to {customer.name}")
            return True
        return False

    # Withdraws money into chosen account
    def withdraw(self, ssn, acc_id, amount) -> bool:
        customer = self.get_customer(ssn)
        if not customer:
            return False
        acc = self.get_account(customer, acc_id)
        if acc:
            if acc.withdraw(amount):
                self.print_success(f"{amount} successfully withdrawed from account id {acc_id} belonging to {customer.name}")
                return True
            else:
                self.print_error(f"Insufficent funds for account id {acc_id} belonging to {customer.name}")
                return False
        return False

    # Closes active account and returns balance of closed account
    def close_account(self, ssn, acc_id) -> int:
        customer = self.get_customer(ssn)
        if not customer:
            return
        acc = self.get_account(customer, acc_id)
        if acc:
            balance = acc.balance
            customer.accounts.remove(acc)
            self.print_success("Account was deleted.")
            return balance

    # Returns all transactions from account if it exists
    def get_all_transactions_by_ssn_acc_id(ssn, acc_id) -> str:
        pass

    # Helper functions to print colored text
    def print_error(self, s) -> None:
        print(f"{colorama.Fore.RED}{s}{colorama.Style.RESET_ALL}")
    
    def print_success(self, s) -> None:
        print(f"{colorama.Fore.GREEN}{s}{colorama.Style.RESET_ALL}")
