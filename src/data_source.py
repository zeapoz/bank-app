from abc import ABC, abstractmethod

from customer import Customer

class DataSource(ABC):
    def __init__(self) -> None:
        pass

    # Establish connection to database
    @abstractmethod
    def datasource_conn(self) -> tuple():
        pass

    # Returns list of all customers and list of increments
    @abstractmethod
    def get_all(self) -> tuple:
        pass

    # Update customers info
    def update_by_id(self, id) -> list:
        pass

    # Find customer based on id
    def find_by_id(self, id) -> Customer:
        pass

    # Removes customer based on id
    def remove_by_id(self, id) -> list:
        pass
