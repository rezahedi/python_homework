# Write your code here.
def hello():
  return "Hello!"

print( hello() )

def greet(name):
  return f"Hello, {name}!"

print ( greet("Reza") )

def calc(firstNumber, secondNumber, operation='multiply'):

  # Catch error before any operation if values are not number
  try:
    x = firstNumber * secondNumber
  except TypeError:
    return "You can't multiply those values!"

  if operation == 'add':
    return firstNumber + secondNumber
  
  if operation == 'subtract':
    return firstNumber - secondNumber
  
  if operation == 'multiply':
    return firstNumber * secondNumber

  if operation == 'divide':
    try:
      return firstNumber / secondNumber
    except ZeroDivisionError:
      return "You can't divide by 0!"
  
  if operation == 'modulo':
    return firstNumber % secondNumber

  if operation == 'int_divide':
    return firstNumber // secondNumber

  if operation == 'power':
    return firstNumber ** secondNumber

  return "Operation not found!"