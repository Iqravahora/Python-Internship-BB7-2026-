def apply_discount(price, percentage=10):
    discount = price * percentage / 100
    
    final_price = price - discount
    print("final price:", final_price)

apply_discount(2000)
apply_discount(1000, percentage = 20)

