from display import *

class Transaction:
    def __init__(self, id, cus_id, acc_id, date, amount) -> None:
        self.id = id
        self.cus_id = cus_id
        self.acc_id = acc_id
        self.date = date
        self.amount = amount
        pass

    def __str__(self) -> str:
        return f"\nAccount ID: {self.acc_id}\nDate: {self.date}\n{self.amount}"

if __name__ == "__main__":
    print_error("This python script is not meant to be run directly, please import in another class!")
    quit()
