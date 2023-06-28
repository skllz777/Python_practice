sandwich_orders = ['chicken', 'bbq', 'beef', 'vegan']
finished_sandwiches = []
while sandwich_orders:
    ready = sandwich_orders.pop()
    print(f"I made your {ready} sendwich")
    finished_sandwiches.append(ready)
for sandwich in finished_sandwiches:
    print(f"Here your {sandwich} sandwich")
