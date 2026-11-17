product = {"pen":20, "Book":150, "Bag":500, "pencil":10, "Bottal":200}

expensive = {k: v for k, v in product.items() if v > 100}
print(expensive)