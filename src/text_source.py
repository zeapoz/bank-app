import os

from data_source import DataSource
from customer import Customer
from account import Account
from transaction import Transaction
from display import *

class TextSource(DataSource):
    def __init__(self, cus_path, trans_path) -> None:
        self.path = cus_path
        self.trans_path = trans_path
        self.datasource_conn()

    # Establish connection to database
    def datasource_conn(self) -> tuple():
        error = False
        for path in (self.path, self.trans_path):
            if not os.path.exists(path):
                error = True
                print_error(f"Error: No database file found in {path}")
                print_error("Changes made will be written to a new file at the path.\n") 
        if error:
            return (False, f"Could not find database file at {path}.")
        return (True, f"Connected successfully to  database at {path}.")

    # Returns list of all customers and list of increments
    def get_all(self) -> tuple:
        customers = []
        increments = [1, 1]
        if not os.path.exists(self.path):
            return customers, increments
        with open(self.path) as file:
            # Open and read file
            lines = file.readlines()
            for line in lines:
                # Seperate customer and acccounts
                data = line.split("#")
                # Create customer
                cus_data = data[0].split(":")
                id = cus_data[0]
                name = cus_data[1]
                ssn = cus_data[2].strip()
                customer = Customer(id, name, ssn)
                customers.append(customer)
                # Set customer id increment
                if int(id) >= increments[0]:
                    increments[0] = int(id) + 1
                # Account information
                for i in range(1, len(data)):
                    acc_data = data[i].split(":")
                    acc_id = acc_data[0]
                    acc_type = acc_data[1]
                    acc_balance = float(acc_data[2])
                    customer.add_account(Account(acc_type, acc_id, acc_balance))
                    # Set increments from datasource to bank
                    if int(acc_id) >= increments[1]:
                        increments[1] = int(acc_id) + 1
        return customers, increments

    # Write current state of customers file at path
    def write_customers_to_file(self, customers) -> None:
        with open(self.path, "w") as file:
            lines = []
            for c in customers:
                s = f"{c.id}:{c.name}:{c.ssn}"
                for a in c.accounts:
                    s += f"#{a.acc_id}:{a.acc_type}:{a.balance}"
                lines.append(f"{s}\n")
            file.writelines(lines)
    
    # Load transactions and return
    def load_transactions(self) -> list:
        transactions = []
        increment = 1
        if not os.path.exists(self.trans_path):
            return transactions, increment
        with open(self.trans_path) as file:
            for l in file.readlines():
                # Split data and assign
                data = l.split(",")
                id = data[0]
                cus_id = data[1]
                acc_id = data[2]
                date = data[3]
                amount = data[4].strip()
                t = Transaction(id, cus_id, acc_id, date, amount)
                transactions.append(t)
                # Set incrementent
                if int(id) >= increment:
                    increment = int(id) + 1
        return transactions, increment

    # Write all transactions to file at path
    def write_transactions_to_file(self, transactions) -> None:
         with open(self.trans_path, "w") as file:
            lines = []
            for t in transactions:
                s = f"{t.id},{t.cus_id},{t.acc_id},{t.date},{t.amount}"
                lines.append(f"{s}\n")
            file.writelines(lines)

if __name__ == "__main__":
    print_error("This python script is not meant to be run directly, please import in another class!")
    quit()
