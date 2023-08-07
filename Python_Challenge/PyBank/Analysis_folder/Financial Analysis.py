#Financial Analysis
import os
import csv

#file path
budget_datacsv=os.path.join("C:/","Users","wambu","Desktop","Python_Challenge","PyBank","Resources_folder", "budget_data.csv")
#list of variables
months=[]
profits=[]
changes=[]

#Read the CSV
with open(budget_datacsv, newline='') as budget_datacsv:
    # CSV reader specifies delimiter and variable that holds data
    csvreader = csv.reader(budget_datacsv, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header and find our values of interest
    for row in csvreader:
        months.append(row[0])
        profits.append(int(float(row[1])))
    # Find average change
    for x in range(1, len(profits)):
        changes.append((int(profits[x]) - int(profits[x-1])))
    # Calculate average revenue change
        changemonths = sum(changes) / len(changes)
    # Calculate min/max dates and averages
    max_date = months[changes.index(max(changes)) + 1]
    min_date = months[changes.index(min(changes)) + 1]

# Printing to terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(months)}")
print(f"Total Profits: ${sum(profits)}")
print(f"Average change:  ${round(changemonths, 2)}")
print(f"The greatest increase is {max_date} (${max(changes)})")
print(f"The greatest decrease is {min_date} (${min(changes)})")

output = os.path.join("C:/","Users","wambu","Desktop","Python_Challenge","PyBank","analysis_folder", "Analysis.txt")

with open(output, "w") as file:
    writer = csv.writer(file)
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total Profits: ${sum(profits)}\n")
    file.write(f"Average change:  ${round(changemonths, 2)}\n")
    file.write(f"The greatest increase is {max_date} (${max(changes)})\n")
    file.write(f"The greatest decrease is {min_date} (${min(changes)})\n")