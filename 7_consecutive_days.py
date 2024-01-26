import pandas as pd

# Specify the path to the external file
file_path = './data.csv'

# Read data into a DataFrame 
# And parsing the time-related columns to date-time format by using 'parse_dates' function
df = pd.read_csv(file_path, parse_dates=['Time', 'Time Out', 'Pay Cycle Start Date', 'Pay Cycle End Date'])

# Calculate the consecutive days worked for each employee
# ASSUMPTION: Each file number is unique
df['Consecutive Days'] = df.groupby('File Number')['Time'].diff().dt.days

# Find employees who have worked for 7 consecutive days
# In 'Consecutive Days' column if the value equals 1 he/she worked for 7 Consecutive days  

result = df[df['Consecutive Days'] == 1].groupby(['Employee Name', 'Position ID']).size()

# Write the result to a separate file called output.txt

with open("./output.txt", 'w') as output_file:
    output_file.write("\n=================================================\n")
    output_file.write("Employees works for 7 Consecutive days:\n")
    output_file.write("=================================================\n")
    for row in result.reset_index().values:
        output_file.write(f"{row[0].replace(",", " ")}, {row[1]} \n")
