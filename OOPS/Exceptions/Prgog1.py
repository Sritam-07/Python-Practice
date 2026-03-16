class axis(Exception):
    pass
min_balance = 5000
balance_amount=7000
def withdraw(required_amt):
    try:
        if(min_balance<=balance_amount-min_balance):
            print("You can wothdraw")
        else:
            obj = axis("you are not allowed")
        raise obj
    except axis as x:
        print(x)
    
withdraw(3000)    