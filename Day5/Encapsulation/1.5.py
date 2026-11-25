class Stack:
    def __init__(self):
        self.__items = [] #private list item
        
    def push(self, items):#add itmes
        self.__items.append(items)
        
    def pop(self):#pop remove last item
        return self.__items.pop()
    
    def __str__(self): #display all current items
        return str(self.__items)
    
s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)


print(s1)
s1.pop()
print(s1)