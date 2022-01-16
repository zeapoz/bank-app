class Account:
    def __init__(self, acc_type, acc_id, balance=0) -> None:
        self.acc_type = acc_type
        self.acc_id = acc_id
        self.balance = balance
    
    def deposit(self, amount) -> None:
        self.balance += amount
    
    def withdraw(self, amount) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
