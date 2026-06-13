class BankAccount:
 def __init__(self, balance):
        self.__balance = balance  
      
 def deposit(self, amount):
   if amount > 0:
        self.__balance += amount

 def withdraw(self, amount):
    if 0 < amount <= self.__balance:
         self.__balance -= amount
    else:
        print("Insufficient funds or invalid amount.")

 def get_balance(self):
    return self.__balance  
                 
# usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)  # Output: Insufficient funds or invalid amount. 
