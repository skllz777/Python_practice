def show_massages(massage):
    sanded = []
    for words in massage:
        print(words)
        sanded.append(words)
    print(sanded)
    print(test)

test = ['hello', 'good night', 'thank you', 'good bye']
show_massages(test[:])