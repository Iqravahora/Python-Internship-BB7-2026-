price = [50,70,100,120,140,150,160,170,190,200]

total = sum(price)
count = len(price)
average = total /count

print("average price is",average)

above_average = [price for price in price if price > average]
print("Above average price:", above_average)


