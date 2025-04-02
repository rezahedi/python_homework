# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# %% 1. Create a DataFrame from a dictionary
import pandas as pd

persons = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(persons)
print(task1_data_frame)

# %% 2. Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# %% 3. Modify an existing column
task1_older = task1_with_salary.copy()
task1_older.loc[:, 'Age'] += 1
print(task1_older)

# %% 4. Save the DataFrame as a CSV file
task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
# %% 1. Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# %% 2. Read data from a JSON file
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# %% 3. Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)