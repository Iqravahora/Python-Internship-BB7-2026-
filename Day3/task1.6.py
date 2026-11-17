numbers = [45,12,34,54,76,23,56,87]
largest = numbers[0]
second = numbers[0]

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n
        print("second largest:",second)