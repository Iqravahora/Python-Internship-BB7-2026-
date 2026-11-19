def get_value(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return None
numbers = [10, 30, 40, 50]

print(get_value(numbers, 2))
print(get_value(numbers, 5))