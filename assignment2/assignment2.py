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