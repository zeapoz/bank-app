import colorama as c

# Helper functions to print colored text
def print_error(s) -> None:
    print(f"{c.Fore.RED}{s}{c.Style.RESET_ALL}")

def print_success(s) -> None:
    print(f"{c.Fore.GREEN}{s}{c.Style.RESET_ALL}")

def print_accent(s) -> None:
    print(f"{c.Fore.BLUE}{s}{c.Style.RESET_ALL}")

if __name__ == "__main__":
    print_error("This python script is not meant to be run directly, please import in another class!")
    quit()
