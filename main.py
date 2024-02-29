def my_calculator(operand1, operand2, operator):
  if (operand1 == "" or operand2 == "" or operator == ""):
      raise ValueError("Error: Values cannot be empty strings")

  operators = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y if y != 0 else float('inf')}

  if operator not in operators:
      raise ValueError("Error: Invalid operator")

  return operators[operator](operand1, operand2)

restart = True
while restart:
  try:
      operandOne = int(input("Enter the first operand: "))
      operator = input("Enter the operator: ")
      operandTwo = int(input("Enter the second operand: "))

      result = my_calculator(operandOne, operandTwo, operator)
      print(f"{operandOne} {operator} {operandTwo} = {result}")

      if input("Do you wish to continue (y/n): ").lower() != 'y':
          restart = False

  except ValueError as ve:
      print(ve)
      if input("Do you want to restart (y/n): ").lower() != 'y':
          restart = False
