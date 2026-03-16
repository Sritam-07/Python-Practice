class axis(Exception):
    def __init__(self, message):
        super().__init__(message)

min_balance = 5000
balance_amount = 7000

def withdraw(required_amt):
    if balance_amount - required_amt >= min_balance:
        print("You can withdraw")
    else:
        raise axis("You are not allowed to withdraw")

withdraw(3000)