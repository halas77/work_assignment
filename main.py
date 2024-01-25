import pandas as pd

# Specify the path to the external CSV file
csv_file_path = './data.csv'

# Read CSV data into a DataFrame
df = pd.read_csv(csv_file_path, parse_dates=['Time', 'Time Out', 'Pay Cycle Start Date', 'Pay Cycle End Date'])

# Calculate the consecutive days worked for each employee
df['ConsecutiveDays'] = df.groupby('Employee Name')['Time'].diff().dt.days

# Find employees who have worked for 7 consecutive days
result = df[df['ConsecutiveDays'] == 1].groupby('Employee Name').size()

# Print the result
with open("./output.txt", 'w') as output_file:
    output_file.write("Employees who have worked for 7 consecutive days: \n")
    for employee in result.index.tolist():
        output_file.write(employee + '\n')


