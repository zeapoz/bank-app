from account import *

class DataSource:
    def __init__(self) -> None:
        pass

    # Establish connection to database
    def datasource_conn() -> tuple(bool, str):
        pass

    # Returns list of all customers
    def get_all() -> list:
        pass

    # Update customers info
    def update_by_id(id) -> list:
        pass

    # Find customer based on id
    def find_by_id(id) -> Account:
        pass

    # Removes customer based on id
    def remove_by_id(id) -> list:
        pass
