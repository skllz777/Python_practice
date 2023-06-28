age = "How old are you?"
age += "\nEnter 'quit' to exit: "
while True:
    message = input(age)
    if message == 'quit':
        break
    age1 = int(message)
    if age1 <= 3:
        print("Cinema is free")
    elif age1 <= 12:
        print("Cinema cost's 10$")
    else:
        print("Cinema cost's 15$")




