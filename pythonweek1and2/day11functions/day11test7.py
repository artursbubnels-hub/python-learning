def calculator(num1, num2, operation):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "//":
    if num2 == 0:
      return "Error: Cannot divide by zero"
    return num1 / num2
  else:
    return "Error: Invalid operation"


print(calculator(10, 5, "+"))  
print(calculator(10, 5, "//"))