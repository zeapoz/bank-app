class Customer:
    def __init__(self, id, name, ssn) -> None:
        self.id = id
        self.name = name
        self.ssn = ssn
        self.accounts = []
    
    def set_name(self, name) -> None:
        self.name = name
    
    def add_account(self, account) -> bool:
        self.accounts.append(account)
        return True
