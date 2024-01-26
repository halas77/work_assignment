import pandas as pd

# Specify the path to the external CSV file
csv_file_path = './data.csv'

# Read CSV data into a DataFrame
df = pd.read_csv(csv_file_path, parse_dates=['Time', 'Time Out', 'Pay Cycle Start Date', 'Pay Cycle End Date'])

# Calculate the duration of each shift
# Convert seconds to hours
df['Shift Duration'] = (df['Time Out'] - df['Time']).dt.total_seconds() / 3600  

# Filter employees who have worked for more than 14 hours in a single shift
filtered_df = df[df['Shift Duration'] > 14]

# Write the result to an external file
with open('output.txt', 'a') as output_file:
    output_file.write("\n====================================================\n")
    output_file.write("Employees work for greater than 14 hours:\n")
    output_file.write("====================================================\n")
    for _, row in filtered_df[['Employee Name', 'Position ID']].iterrows():
        output_file.write(f"{row['Employee Name'].replace(',', '')}, {row['Position ID']}\n")

