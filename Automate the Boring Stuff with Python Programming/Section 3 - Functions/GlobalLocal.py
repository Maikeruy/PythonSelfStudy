eggs = 5


def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)


spam()
