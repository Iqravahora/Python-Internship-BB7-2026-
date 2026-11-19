def safe_devision(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "Error: not divide by zero"
    except TypeError:
        return "Error: enter valid number only!"
    
    
print(safe_devision(10, 2))
print(safe_devision(10, 0))
print(safe_devision(10, "a"))
print(safe_devision("10", 2))
    
    