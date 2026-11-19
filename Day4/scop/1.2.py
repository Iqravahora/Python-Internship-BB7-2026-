def make_greeting(language):
    def greet(name):
        if language == "hindi":
            print(f"good morning , {name}")
        else:
            print(f"good morning, {name}")
    return greet
    
hindi_greet = make_greeting("hindi")
english_greet = make_greeting("english")

hindi_greet("iqra")
english_greet("iqu")




