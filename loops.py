'''
LOOPS
- A loop occurs when a the same  process is executed repeatedly until a particular set of conditions is met

TYPES OF LOOPS
1. While loop
2. for in loop
3. Nested loop


Components of a loop
1. Condition: This is the satement that determines if the loop should be executed. eg x < 7, it is usually a boolian ststemnt: One  of that return either a True or False value
2. Initializer: Conditions a value that can either be incremated. By default the initializer should start at a value 0
3. Incremation: This is when the intialized value is incremented(+1) to be able to determine the number of loops done.

The components above in python will only apply to a while loop, however for a for in loop this will be different as will be shown.
'''

# Example 1
# While loop 
i = 0 #initializer
while(i < 5.2): # The condition is placed inside the while() brackets
    print(f"lap {i}")
    i += 1 #Incrementation. This is the same as saying i = i + 1
    
#NB: The i on the right hand side contains the initial value of i eg: 0


# Example 2
while(True):
    username = input("Input your name: ")
    print(username)
    if username == "x":
        break
    
    '''
    1. .lower()- This is used to convert a string into a lowercase
    Eg: username = "J"
        new_username = username.lower()  "j"
    2. .upper()- This is used to convert a string into uppercase.
    3. isdigit()- Is used to check if a string comprises of digits    
    '''