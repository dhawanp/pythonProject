'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

#The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
#
# Example
# Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
#
# Example
# In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
#
# Example
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Raise an exception
'''
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
#
# Example
# Raise an error and stop the program if x is lower than 0:

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# 
# To throw (or raise) an exception, use the raise keyword.
# 
# Example
# Raise an error and stop the program if x is lower than 0:
'''
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# We can also raise a TypeError
x='hello'
if not type(x) is int:
    raise TypeError("Only Integers Allowed")
