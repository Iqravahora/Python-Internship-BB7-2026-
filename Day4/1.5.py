from functools import reduce
numbers = [3,9,2,7,5]
largest = reduce(lambda a, b: a if a>b else b, numbers)
print(largest) 