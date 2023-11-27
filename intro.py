print("Hello Python!")

num1 = 1
num2 = 2

print(num1+num2)

"""
Multiple line comment
"""
# Single comment


# Implementing if conditional statemnt in python
num = input("Input a number: ")
integer_num = int(num)

if(integer_num%2 == 0 and integer_num%3 == 0):
    print("This number is both divisible by 2 and 3")
elif(integer_num%2 == 0):
    print(f"{integer_num} is an even number")
elif(integer_num%3 == 0):
    print(f"{integer_num} is divisible by 3")
else:
    print(f"{integer_num} not divisible by both 2 or 3")

        
    