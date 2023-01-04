# Define a function that takes in two numbers and performs the desired operation
def calculate(num1, num2, operation):
  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    # Make sure the second number is not zero to avoid a ZeroDivisionError
    if num2 != 0:
      return num1 / num2
    else:
      return "Cannot divide by zero!"

# Test the function with some examples
# print(calculate(1, 2, "add")) # Should print 3
# print(calculate(5, 2, "subtract")) # Should print 3
# print(calculate(3, 4, "multiply")) # Should print 12
# print(calculate(10, 5, "divide")) # Should print 211
# print(calculate(10, 0, "divide")) # Should print "Cannot divide by zero!"
print(calculate(200, 100,"divide"))