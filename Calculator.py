#Calculator
#Add
from art import logo
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 -n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}



def calculator():
  print(logo)
  still_working = True
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  while still_working:
    operator_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operator_symbol](num1,num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    
    keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation: ").lower()
    print("\n")
    if keep_going == 'n':
      still_working = False
      calculator()
    else:
      num1 = answer


calculator()