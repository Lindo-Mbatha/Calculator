from CalLogo import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {"+": add,
"-": subtract,
"*": multiply,
"/": divide}

print(logo)

num1 = float(input("What is the first number? "))

for key in operations:
  print(key)
operation_key = input("Pick a operation from the list above: ")

num2 = float(input("What is the second number? "))

calculation_function = operations[operation_key]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_key} {num2} = {answer}")