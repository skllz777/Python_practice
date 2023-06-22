pizzas = ['Pepperoni', 'Margarita', 'Diablo']
friend_pizzas = pizzas[:]
friend_pizzas.append("Four cheeses")
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friends favorite pizzas are:")
for f_pizza in friend_pizzas:
    print(f_pizza)