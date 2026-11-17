words = ["apple", "banana", "cherry", "carrot"]

grouped = {}
for w in words:
    grouped.setdefault(w[0], []).append(w)
    
print(grouped)