
# Week 4 Assignment - My First Toolbox

# Function 1: Double a number
def double(number):
    return number * 2


# Function 2: Check if a learner passes
def is_pass(score):
    return score >= 50


# Function 3: Greet a person
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Test the functions
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
