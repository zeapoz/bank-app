class Transaction:
    def __init__(self, id, cus_id, acc_id, date, amount) -> None:
        self.id = id
        self.cus_id = cus_id
        self.acc_id = acc_id
        self.date = date
        self.amount = amount
        pass

    def __str__(self) -> str:
        return f"{self.id} {self.cus_id} {self.acc_id}\n{self.date}\n{self.amount}"
