'''
Let's write some if statements! 
If statements are used to control the flow of a program.
If a condition is True, the code inside the if statement will run.
If the condition is False, then the code inside the if statement will be skipped.
The condition MUST be a boolean value. 
'''

if 1 == 2:
    print("Will this code run?")
else:
    print("Does this code run?")

# Will this code run?
if "Hello":
    print("Will this code run?")



# We can also have "else if" statements.
# These are used to check multiple conditions.
# If the first condition is False, the code inside the "else if" statement will run.
if 1 == 2:
    print("Will this code run?")
elif 1 == 1:
    print("Does this code run?")
else:
    print("What about this code?")