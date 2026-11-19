def outer():
    status = "pending"
    
    def inner():
        nonlocal status
        status = "Finish"
        
    inner()
    print("last part:", status)
    
outer()