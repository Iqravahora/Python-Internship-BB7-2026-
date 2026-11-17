def marks(m):
    low = min(m)
    high = max(m)
    avg = sum(m) / len(m)
    
    return low,high,avg

m = [40 , 60, 70, 80, 90]

a, b, c = marks(m)

print("lowest:",a)
print("highest:",b)
print("average:",c)

