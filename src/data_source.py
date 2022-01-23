import os

from customer import Customer
from account import Account
from display import *

class DataSource:
    def __init__(self, path) -> None:
        self.path = path
        self.datasource_conn()

    # Establish connection to database
    def datasource_conn(self) -> tuple():
        if os.path.exists(self.path):
            return (True, f"Connected successfully to databse at {self.path}.")
        else:
            print_error("Error: No database file found in \"./data.txt\"")
            print_error("Changes made will be written to a new file at the path.") 
            return (False, f"Could not find database file at {self.path}.")

    # Returns list of all customers and list of increments
    def get_all(self) -> tuple:
        customers = []
        increments = [0, 0]
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
                    print(increments)
        return customers, increments

    # Write current state file at path
    def write_customers_to_file(self, customers) -> None:
        with open(self.path, "w") as file:
            lines = []
            for c in customers:
                s = f"{c.id}:{c.name}:{c.ssn}"
                for a in c.accounts:
                    s += f"#{a.acc_id}:{a.acc_type}:{a.balance}"
                lines.append(f"{s}\n")
            file.writelines(lines)

    # Update customers info
    def update_by_id(self, id) -> list:
        pass

    # Find customer based on id
    def find_by_id(self, id) -> Customer:
        pass

    # Removes customer based on id
    def remove_by_id(self, id) -> list:
        pass
