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
print(f"Subtraction={subtract_result}")

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

# def divisible(number):
#     if number%7 == 0:
#         print("This Number is divsible by 7")
#     else:
#         print("Try again ")
# number =int(input("Enter the number:"))
# divisible(number)

def divisible(x, y):
    if(x%y ==0):
        return f"{x} is divisible by {y}"
    return f"{x} is not divisible by {y}"

print("CHECK DIVISIBILITY BETWEEN 'X' AND 'Y'\n")
print("Press 'x' to exit")

while(True):
    x = input("input value for x: ")
    if x.upper() == "X":
        break
    y = input("Input value of Y: ")
    
    if x.isdigit() and y.isdigit():
        input_x = int(x)
        input_y = int(y)
        result = divisible(input_x, input_y)
        print(result)
    else:
        print("INVALID INPUTS TRY AGAIN ") 