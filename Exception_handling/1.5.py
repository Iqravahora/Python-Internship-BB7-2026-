class outofRangeError(Exception):
    pass
while True:
    try:
        num = int(input("enter a number 1 to 10"))
        if num < 1 or num > 10:
            raise outofRangeError("Number must betwee 1 to 10")
        print(f"Great!valid number", num)
        break
    except ValueError as e:
        print("Invalid input:", e)
       