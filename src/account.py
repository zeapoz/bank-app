from display import *

class Account:
    def __init__(self, acc_type, acc_id, balance=0) -> None:
        self.acc_type = acc_type
        self.acc_id = acc_id
        self.balance = balance
    
    def deposit(self, amount) -> bool:
        self.balance += amount
        return True
    
    def withdraw(self, amount) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def __str__(self) -> str:
        return f"{self.acc_type} {self.acc_id} {self.balance}"

if __name__ == "__main__":
    print_error("This python script is not meant to be run directly, please import in another class!")
    quit()
