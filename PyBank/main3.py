import os
import csv

PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")

#define arrays/variables
total = 0
months = []
margins = []
change = []

# Open and read csv
with open(PyBank_csv, newline="", encoding= 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvfile)

    for row in csvreader:
        months.append(row[0])
        total_months = len(months)
        total += float(row[1])
        margins.append(int(row[1]))

    for x in range(len(margins)):
        if x + 1 < len(margins):
            change.append(margins[x+1] - margins[x])

    ave_change = sum(change) / len(change)
    max_value = max(change)
    min_value = min(change)

print(total_months)
print(total)
print(ave_change)
print(max_value)
print(min_value)