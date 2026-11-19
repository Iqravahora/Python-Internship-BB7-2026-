def make_validator(min_value):
    def check(number):
        return number >= min_value
    return check

check1 = make_validator(10)
check2 = make_validator(50)

print(check1(40))
print(check1(5))

print(check2(60))
print(check2(30))

