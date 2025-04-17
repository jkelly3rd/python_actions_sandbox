import csv

# Open and sort the CSV file by the 'emp' field
def sort_csv_by_emp(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        sorted_rows = sorted(reader, key=lambda row: row['Total Employees'])
    
    # Print sorted rows
    for row in sorted_rows:
        print(row)

# Specify the file path
file_path = 'data/ny.csv'
sort_csv_by_emp(file_path)