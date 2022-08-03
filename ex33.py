'''
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
'''
# Study Drills
"""
1. Convert this while-loop to a function that you can call, and replace 6 in the test ( i < 6 ) with a
variable.
"""

def whileLoopFunction(numbers,till,i,incrementValue):
    while i < till:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incrementValue 
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

numbers = []
# 2. Use this function to rewrite the script to try different numbers.
till = input("Loop until what number: ")
i = 0

# Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
incrementValue = input("What is the incrementValue for loop: ")
# 4. Rewrite the script again to use this function to see what effect that has.
numbers = whileLoopFunction(numbers,int(till),i,int(incrementValue))

print("The numbers: ")

for num in numbers:
    print(num)

# 5. Write it to use for-loops and range . Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
# If we don't have the incrementor when while loop is used the program goes on a infinite processing
