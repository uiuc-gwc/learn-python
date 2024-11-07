'''
Let's write some if statements! 
If statements are used to control the flow of a program.
If a condition is True, the code inside the if statement will run.
If the condition is False, then the code inside the if statement will be skipped.
The condition MUST be a boolean value. 
'''

if 1 == 2:
    print("one equals two")
else:
    print("one does not equal two")

# Will this code run?
if "Hello":
    print("if hello")



# We can also have "else if" statements.
# These are used to check multiple conditions.
# If the first condition is False, the code inside the "else if" statement will run.
if 1 == 2:
    print("one equals two")
elif 1 == 1:
    print("one equals one")
else:
    print("else!!")
