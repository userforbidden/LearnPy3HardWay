def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a/b


print("Let's do some math with just functions!")

age = add(30,1)
height = subtract(183,4)
weight = multiply(29,5)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A Puzzle for the extra credit, type it anyway.
print("Here is a puzzle.")

what = subtract(add(height, multiply(weight, divide(iq,2))),age)

print(f"That becomes: {what} Can you do it by hand?")
