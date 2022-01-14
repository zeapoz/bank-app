class Account:
    def __init__(self, acc_type, acc_number, balance=0) -> None:
        self.acc_type = acc_type
        self.acc_number = acc_number
        self.balance = balance
