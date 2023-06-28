sandwich_orders = ['pastarami', 'chicken', 'pastarami', 'bbq', 'beef', 'pastarami', 'vegan']
finished_sandwiches = []
print("Pastarami is end")
while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('pastarami')
while sandwich_orders:
    ready = sandwich_orders.pop()
    print(f"I made your {ready} sendwich")
    finished_sandwiches.append(ready)
for sandwich in finished_sandwiches:
    print(f"Here your {sandwich} sandwich")
