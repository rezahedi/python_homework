import csv
import os
import custom_module
from datetime import datetime

def read_employees(file='../csv/employees.csv', rowType=lambda row:row):
  employees = {}
  myList = []

  try:
    with open(file, 'r') as file:
      isKeys = True
      reader = csv.reader(file)
      for row in reader:
        if isKeys:
          employees['fields'] = row
          isKeys = False
          continue
        myList.append( rowType(row) )
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

def sort_by_last_name():
  employees['rows'].sort(key=lambda row : row[column_index('last_name')])
  return employees['rows']

def employee_dict(row):
  myDict = dict(zip(employees['fields'], row))
  myDict.pop('employee_id')
  return myDict
print(employee_dict(employees['rows'][3]))

def all_employees_dict():
  allEmployees = {}
  index = 0
  for row in employees['rows']:
    allEmployees[ row[column_index('employee_id')] ] = employee_dict(row)
    index += 1
  return allEmployees
print(all_employees_dict())

def get_this_value():
  return os.getenv('THISVALUE')

def set_that_secret(new_secret):
  custom_module.set_secret(new_secret)
set_that_secret('spiderman!')
print(custom_module.secret)

def read_minutes():
  minutes1 = read_employees('../csv/minutes1.csv', lambda row:tuple(row))
  minutes2 = read_employees('../csv/minutes2.csv', lambda row:tuple(row))
  return minutes1, minutes2
minutes1, minutes2 = read_minutes()

def create_minutes_set():
  m1 = set(minutes1['rows'])
  m2 = set(minutes2['rows'])
  return m1.union(m2)
minutes_set = create_minutes_set()

def create_minutes_list():
  minutesList = list(map(
    lambda row:(row[0], datetime.strptime(row[1], "%B %d, %Y")),
    minutes_set
  ))
  return minutesList
minutes_list = create_minutes_list()

def write_sorted_list():
  minutes_list.sort(key=lambda row : row[1])
  minutesList = list(map(
    lambda row: (row[0], datetime.strftime(row[1], "%B %d, %Y")),
    minutes_list
  ))
  with open('./minutes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(minutes1['fields'])
    writer.writerows(minutesList)
  return minutesList
write_sorted_list()
