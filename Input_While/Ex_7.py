responces = {}
responces_active = True
while responces_active:
    name = input("Please enter your name: \n")
    responce = input("Enter your responce: \n")
    responces[name] = responce
    repeat = input("Do you want to continue? Please enter Yes or No: \n")
    if repeat.title() == "No":
        responces_active = False
for name, responce in responces.items():
    print(f"{name.title()} would like to go to the {responce.title()}.")