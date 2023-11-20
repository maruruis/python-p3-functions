def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name=None):
    if name is None:
        print("Hello, programmer!")
    else:
        print(f"Hello, {name}!")

def add(a, b):
    return a + b

def halve(n):
    return n / 2
