# Decorators

cust = {
    'first_name': "John",
    'last_name': "McDermott",
    'present_customer': True,
    'account_balance': 100
}

def customer(f):
    def check_customer(*args, **kwargs):
        if args[0]['present_customer']:
            return f(*args, **kwargs)
    return check_customer

def account(f):
    def check_balance(*args, **kwargs):
        if args[0]['account_balance'] > 100:
            return f(*args, **kwargs)
        else:
            return print("Customer doesn't have enough amount to withdraw")
    return check_balance

@customer
def valid_customer(cust1):
    print("Customer Exists")

valid_customer(cust)

@account
def money_withdraw(cust1):
    print("Customer's account has sufficient balance")
    print("Customer can withdraw amount")

money_withdraw(cust)
