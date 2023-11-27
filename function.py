def say_hello():
    print("Hello!!!")

def addition(x, y):
    result = x+y
    return result

add_result = addition(10, 11)
print(add_result)

#subtraction, multiplication, isEven, division

def subtraction(x, y):
    result = x-y
    return result
subtract_result = subtraction(45, 28)
print(f"Subtraction{subtract_result}")

def multiplication(x, y):
    result = (x * y)
    return result
multiply_result = multiplication(45, 28)
print(f"Multiplication={multiply_result}")

def division(x, y):
    result = (x / y)
    return result
division_result = division(48, 12)
print(f"Division={division_result}")

def is_even(x):
    if(x%2 == 0):
       return True
    return False
result = is_even(13)
print(f"Is Even={result}")
