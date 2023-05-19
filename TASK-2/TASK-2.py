import csv
from collections import defaultdict

# Defining the files paths of the CSV files
departments_file = 'Departments.csv'
employees_file = 'Employees.csv'
salary_file = 'Salaries.csv'

# Reading the department csv file data
departments = {}
with open(departments_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        departments[row['ID']] = row['NAME']

# Reading the employees csv file data
employees = defaultdict(list)
with open(employees_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees[row['ID']].append(row['DEPT ID'])

# Reading the salaries csv file data
salary_data = defaultdict(list)
with open(salary_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        salary_data[row['EMP_ID']].append(int(row['AMT (USD)']))

# Calculating average monthly salary for each department
department_salary = {}
for dept_id, emp_ids in employees.items():
    total_salary = sum(sum(salary_data[emp_id]) for emp_id in emp_ids)
    avg_salary = total_salary / len(emp_ids)
    department_salary[dept_id] = avg_salary

# Fetching top 3 departments by average monthly salary
top_departments = sorted(department_salary.items(), key=lambda x: x[1], reverse=True)[:3]

# Printing the results
print("Top 3 Departments:")
for dept_id, avg_salary in top_departments:
    name = departments[dept_id]
    print(f"Department: {name}")
    print(f"Average Monthly Salary: {avg_salary:.2f}")
    print()
