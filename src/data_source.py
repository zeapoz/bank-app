from customer import Customer
from account import Account
from display import *

class DataSource:
    def __init__(self, path) -> None:
        self.path = path
        self.datasource_conn(path)

    # Establish connection to database
    def datasource_conn(self, path) -> tuple():
        try:
            # TODO Make prettier and less redundant
            file = open(path)
            file.close()
            return (True, f"Connected successfully to databse at {path}.")
        except:
            print_error("Error: No database file found in \"./data.txt\"")
            print_error("Changes made will be written to a new file at the path.") 
            return (False, f"Could not find database file at {path}.")

    # Returns list of all customers
    def get_all(self, file) -> list:
        customers = []
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
            # Account information
            for i in range(1, len(data)):
                acc_data = data[i].split(":")
                acc_id = acc_data[0]
                acc_type = acc_data[1]
                acc_balance = float(acc_data[2])
                customer.add_account(Account(acc_type, acc_id, acc_balance))
                # TODO Set increments from datasource to bank
        file.close()
        return customers

    # Update customers info
    def update_by_id(id) -> list:
        pass

    # Find customer based on id
    def find_by_id(id) -> Customer:
        pass

    # Removes customer based on id
    def remove_by_id(id) -> list:
        pass
