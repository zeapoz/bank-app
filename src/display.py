import colorama as c

# Helper functions to print colored text
def print_error(s) -> None:
    print(f"{c.Fore.RED}{s}{c.Style.RESET_ALL}")

def print_success(s) -> None:
    print(f"{c.Fore.GREEN}{s}{c.Style.RESET_ALL}")
