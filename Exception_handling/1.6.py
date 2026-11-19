def process_order(order):
    try:
        item=order["item"]
        price=order["price"]
        
    except KeyError:
        print("Error:Expected key is missing")
    else:
        print("item:",item)
        print("price:",price)
    finally:
        print("complete process")
        
order={"item":"Book","price":300}
process_order(order)