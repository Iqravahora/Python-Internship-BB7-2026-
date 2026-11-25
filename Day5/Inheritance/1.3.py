class Account:
    def get_interest_rate(self):
        return 3
    
class SavingsAccount(Account):
    def get_interest_rate(self):
        return 4
    
class FixedDeposit(Account):
    def get_interest_rate(self):
        return 6
    
s1 = Account()
s2 = SavingsAccount()
s3 = FixedDeposit()

accounts = [s1, s2, s3]

for account in accounts:
    print(account. get_interest_rate())
