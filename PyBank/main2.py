import os
import csv

PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

#find total months
    Data=list(csvreader)
    total_months = len(Data)
    print(total_months)
   # print(Data)

#Find total profit/losses
#margins = [profit for profit in Data += float(row[1])]

#print(margins)

margins = 0
for row in Data:
    margins += float(row[1])
print(margins)

change = 0.00
print(change)
for row in Data:
    change = sum(float(row[1,1]) - float(row[0,1]))
    