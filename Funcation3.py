balance=10000

def deposit():
    global balance
    amount=5000
    balance+=amount
    print("Deposit Amount:", amount)
    print("Balance:", balance)

def withdraw():
    global balance 
    amount=50000
    balance-=amount
    print("Withdraw Amount:",amount)
    print("balance:",balance)

deposit()
withdraw()
