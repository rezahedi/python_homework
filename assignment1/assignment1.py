# Task 1: Hello world
def hello():
  return "Hello!"

print( hello() )

# Task 2: Greet with a Formatted String
def greet(name):
  return f"Hello, {name}!"

print ( greet("Reza") )

# Task 3: Calculator
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

# Task 4: Data Type Conversion
def data_type_conversion(value, dataType):
  if dataType == 'str':
    return str(value)

  try:
    if dataType == 'float':
      return float(value)
    elif dataType == 'int':
      return int(value)
  except ValueError:
    return f"You can't convert {value} into a {dataType}."

  return f"Data type `{dataType}` not found!"

# Task 5: Grading System, Using *args
def grade(*args):
  try:
    average = sum(args) / len(args)
  except TypeError:
    return "Invalid data was provided."
  
  match average:
    case value if value >= 90:
      return 'A'
    case value if value >= 80:
      return 'B'
    case value if value >= 70:
      return 'C'
    case value if value >= 60:
      return 'D'
  return 'F' 

# Task 6: Use a For Loop with a Range
def repeat(string, count):
  repeatedString = ""
  for i in range(count):
    repeatedString += string

  return repeatedString

# Task 7: Student Scores, Using **kwargs
def student_scores(type, **kwargs):
  if type == "mean":
    return sum(kwargs.values()) / len(kwargs)

  if type == "best":
    highestScore = 0
    name = ""
    for key, value in kwargs.items():
      if value > highestScore:
        highestScore = value
        name = key
    return name

# Task 8: Titleize, with String and List Operations
def titleize(string):
  littleWords = ['a', 'on', 'an', 'the', 'of', 'and', 'is', 'in']

  words = string.split()

  words[0] = words[0].capitalize()
  words[-1] = words[-1].capitalize()

  for i, word in enumerate(words):
    if word not in littleWords:
      words[i] = word.capitalize()

  return " ".join(words)
