class InvalidAgeError(Exception):
    pass
def register_user(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age!Age between 0 and 20.")
    else:
        print("Registration completed")
        
register_user(15)
register_user(120)