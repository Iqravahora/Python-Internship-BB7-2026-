def build_invoice(name, *prices, **details):
    total = sum(prices)
    
    print("name:", name)
    print("total", total)
    print("Details:", details)
    
build_invoice("iqra", 100, 200, 300, discount=50, tax=10)