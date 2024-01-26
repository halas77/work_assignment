import pandas as pd

# Specify the path to the external CSV file
csv_file_path = './data.csv'

# Read CSV data into a DataFrame
df = pd.read_csv(csv_file_path, parse_dates=['Time', 'Time Out', 'Pay Cycle Start Date', 'Pay Cycle End Date'])

# Sort the DataFrame by 'Employee Name' and 'Time' for consecutive shift calculations
df = df.sort_values(['Employee Name', 'Time'])

# Calculate the time difference between consecutive shifts for each employee
df['Time Difference'] = df.groupby('File Number')['Time'].diff()

# Filter employees with less than 10 hours and greater than 1 hour of time difference between shifts
filtered_df = df[(df['Time Difference'] < pd.Timedelta(hours=10)) & (df['Time Difference'] > pd.Timedelta(hours=1))]

# Display the result
with open('./output.txt', 'a') as output_file:
    output_file.write("\n====================================================================\n")
    output_file.write("Employees with less than 10 hours but greater than 1 hour between shifts:\n")
    output_file.write("====================================================================\n")

    # To keep track of unique names
    unique_names = set()  

    # Iterate in the filetred data to write the output in external file
    for _, row in filtered_df[['Employee Name', 'Position ID']].iterrows():
        if row['Employee Name'] not in unique_names:
            output_file.write(f"{row['Employee Name'].replace(',', ' ')}, {row['Position ID']} \n")
            unique_names.add(row['Employee Name'])


