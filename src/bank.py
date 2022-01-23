import datetime

from customer import Customer
from account import Account
from transaction import Transaction
from data_source import DataSource
from display import *

class Bank:
    def __init__(self) -> None:
        welcome_s = "| Welcome to the bank application! |"
        print("-" * len(welcome_s))
        print(welcome_s)
        print("-" * len(welcome_s))
        # Transaction and increments
        self.transactions = []
        self.trans_id_increment = 1
        self.cus_id_increment = 1
        self.acc_id_increment = 1
        # Create connection to a generic data source
        self.data_source = DataSource("./data.txt")
        # Load data
        self.customers = self._load("./data.txt")

    # Reads text file into customer list
    def _load(self, path) -> list:
        # Call DataSource method to get all customers into internal memory
        return self.data_source.get_all(open(path))

    # Write current state file at path
    def write_to_file(self, path) -> None:
        file = open(path, "w")
        lines = []
        for c in self.customers:
            s = f"{c.id}:{c.name}:{c.ssn}"
            for a in c.accounts:
                s += f"#{a.acc_id}:{a.acc_type}:{a.balance}"
            lines.append(f"{s}\n")
        file.writelines(lines)
        file.close()

    # Return all customers in dict {Social Security Number: name}
    def get_customers(self) -> dict:
        if not self.customers:
            return
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
            print_success("New customer successfully added.")
            return True
        print_error("Error: Social security number already exists.")
        return False

    # Fetches customer based on social security number, optional flag to warn if not found
    def get_customer(self, ssn, warn=True) -> Customer:
        customers = self.get_customers()
        if not customers:
            return None
        customer = customers.get(ssn)
        if customer:
            customer = customer[1]
            return customer
        if warn:
            print_error("Warning: No customer with that social security number.")
        return None

    # Returns a list of customers information
    def get_customer_info(self, ssn) -> list:
        customer = self.get_customer(ssn)
        if not customer:
            return
        info = [customer.name, customer.ssn]
        return info

    # Changes customer name if ssn exists in database
    def change_customer_name(self, name, ssn) -> bool:
        customer = self.get_customer(ssn)
        if not customer:
            return
        customer.set_name(name)
        return True

    # Removes customer and returns that which was removed
    def remove_customer(self, ssn) -> list:
        customer = self.get_customer(ssn)
        if not customer:
            return []
        for acc in customer.accounts:
            acc_id = acc.acc_id
            self.close_account(ssn, acc_id)
        self.customers.remove(customer)
        print_success(f"Successfully removed customer {customer.name}")
        # TODO return what was removed

    # Adds an account to specified customer
    def add_account(self, ssn) -> str:
        customer = self.get_customer(ssn)
        if not customer:
            return
        account = Account("debit account", str(self.acc_id_increment))
        self.acc_id_increment += 1
        if customer.add_account(account):
            print_success(f"Successfully added new account to {customer.name}")
        else:
            print_error(f"Could not add new account to {customer.name}")

    # Returns account belonging to customer
    def get_account(self, customer, acc_id) -> Account:
        for acc in customer.accounts:
            if acc.acc_id == acc_id:
                return acc
        print_error("Error: Account id not matching customers.")
        return None

    # Deposits money into chosen account
    def deposit(self, ssn, acc_id, amount) -> bool:
        customer = self.get_customer(ssn)
        if not customer:
            return
        acc = self.get_account(customer, acc_id)
        if acc and acc.deposit(amount):
            self.add_transaction(ssn, acc_id, amount)
            print_success(f"{amount} successfully deposited into account id {acc_id} belonging to {customer.name}")
            return True
        return False

    # Withdraws money into chosen account
    def withdraw(self, ssn, acc_id, amount) -> bool:
        customer = self.get_customer(ssn)
        if not customer:
            return False
        acc = self.get_account(customer, acc_id)
        if not acc:
            return False
        if acc.withdraw(amount):
            self.add_transaction(ssn, acc_id, amount, True)
            print_success(f"{amount} successfully withdrawed from account id {acc_id} belonging to {customer.name}")
            return True
        else:
            print_error(f"Insufficent funds for account id {acc_id} belonging to {customer.name}")
            return False

    # Closes active account and returns balance of closed account
    def close_account(self, ssn, acc_id) -> int:
        customer = self.get_customer(ssn)
        if not customer:
            return
        acc = self.get_account(customer, acc_id)
        if not acc:
            return
        balance = acc.balance
        customer.accounts.remove(acc)
        print_success("Account was deleted.")
        return balance

    # Returns all transactions from account if it exists
    def get_all_transactions_by_ssn_acc_id(self, ssn, acc_id) -> list():
        customer = self.get_customer(ssn)
        transactions = []
        for t in customer.transactions:
            if t.acc_id == acc_id:
                transactions.append(t)
        return transactions

    def add_transaction(self, ssn, acc_id, amount, withdraw=False) -> None:
        now = datetime.datetime.now()
        if withdraw:
            amount *= -1
        transaction = Transaction(self.trans_id_increment, ssn, acc_id, now, amount)
        self.transactions.append(transaction)
        # Add transaction to customer as well
        customer = self.get_customer(ssn)
        customer.add_transaction(transaction)
        # TODO Write transactions to file
