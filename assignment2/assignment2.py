import csv

def read_employees():
  employees = {}
  myList = []

  try:
    with open('../csv/employees.csv', 'r') as file:
      isKeys = True
      reader = csv.reader(file)
      for row in reader:
        if isKeys:
          employees['fields'] = row
          isKeys = False
          continue
        myList.append(row)
      employees['rows'] = myList

  except Exception as e:
    print(e)

  return employees

employees = read_employees()
print(employees)

def column_index(fieldName):
  try:
    return employees['fields'].index(fieldName)
  except:
    return -1
employee_id_column = column_index('employee_id')

def first_name(rowNumber):
  try:
    colIndex = column_index('first_name')
    return employees['rows'][rowNumber][colIndex]
  except:
    return ''
  
def employee_find(employee_id ):
  def employee_match (row):
    return int(row[employee_id_column]) == employee_id

  matches=list(filter(employee_match, employees["rows"]))
  return matches

def employee_find_2(employee_id):
  matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
  return matches