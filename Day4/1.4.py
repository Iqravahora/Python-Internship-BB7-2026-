usernames = ["jay", "sneh", "vijay", "viraj"]

result = list(filter(lambda u: len(u) >=4, usernames))

print("All:", usernames)
print("Filtered:", result)