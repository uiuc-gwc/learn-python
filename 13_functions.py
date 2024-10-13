# When there's a task we're repeating over and over again, we can make it a function! 
# (this is equivalent to a myBlock in scratch!)

def say_hello():
    print("Hello!")

# Now we can call this function whenever we want to say hello!
say_hello()
say_hello()
say_hello()


# Functions can also take arguments.
# Arguments are values that we pass to the function.
# For example:
def say_something(something):
    print(something)

# Now we can call this function with a string argument.
say_something("Hello!")
say_something("Goodbye!")
say_something("How are you?")
say_something("I'm a function!")

# Functions can also return values.
# For example:
def add(a, b):
    return a + b

# Now we can call this function and get the result.
result = add(3, 4)
print(result)
print(add(7, 9))