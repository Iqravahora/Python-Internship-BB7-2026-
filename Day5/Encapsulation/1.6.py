class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Diffrent currencies")
        return self.amount < other.amount
    
    
    def __gt__(self,other):
        if self.currency != other.currency:
            raise ValueError("another currencies")
        return self.amount > other.amount
    
    c1 = currencies
    
        
        