ad = '\nPlease, choose the topping what you want to add'
ad += '\nIf you finish, please enter "quit": '
while True:
    topping = input(ad)
    if topping == 'quit':
        break
    else:
        print(f"We added {topping} to your order, thank you!")