status = "Global"

def outer():
    status = "Outer"
    
    def inner():
        status = "Inner"
        print("Inner status:", status)
        
    inner()
    print("Outer status:", status)
    
outer()
print("Global status:", status) 