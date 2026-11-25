class wallet:
    def __init__(self, balance):
        self.__balance=balance
        
    def deposit(self):
        amount = int(input("Enter amount to deposit:"))
        if amount < 0:
            print("Cannot deposit")
        else:
            self.__balance+=amount
            print("Amount Deposit")
            
    def withdraw(self):
        Amount = int(input("enter amount to deposit:"))
        if Amount < 0 or Amount > self.__balance:
            print("cannot withdraw")
        else:
            self.__balance -=Amount
            print("amount withdraw")
            
    @property
    def balance(self):
        return self.__balance
    
    
w1 = wallet(9000)
w1.deposit()
w1.withdraw()
print("Amount is:", w1.balance)
    
            
    
    
    