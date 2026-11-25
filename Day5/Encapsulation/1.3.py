class Inventory:
    def __init__(self):
        self.items = ["pen", "Book", "pencil"]
    
    #return number of item 
    def __len__(self):
        return len(self.items)
    
    #return item using index
    def __getitem__(self, index):
        return self.items[index]
    
i = Inventory() #i call the len method
print(i [0]) #return first item
print(i [1])
