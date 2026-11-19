count = 0
def my_function():
    global count 
    count = count + 1
    print(f"function called {count} times")
    
my_function()
my_function()
my_function()
my_function()
my_function()

print(f"final count: {count}")