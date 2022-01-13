class Customer:
    def __init__(self, id, name, ssn) -> None:
        self.id = id
        self.name = name
        self.ssn = ssn
    
    def set_name(self, name) -> None:
        self.name = name
