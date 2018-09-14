# Import Dependencies
import os
import csv

# Import the books.csv file as a DataFrame
BankData = os.path.join("budget_data.csv")

# Create Lists Data and set Varaibles
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
total_net_profit = 0
net_change = 0


with open(BankData, newline="") as FinancialData:
    csvreader = csv.reader(FinancialData, delimiter=",")

# find the number of months
#read the header row
    header = next(csvreader)
    first_row = next(csvreader)
    
    for row in csvreader:
            total_months = total_months + 1
            total_net_profit = total_net_profit + int(row[1])

            previous_net = int(first_row[1])
            net_change = int(row[1]) - previous_net
            previous_net = int(row[1])
                     
            net_change_list = net_change_list + [net_change]

##The average change in "Profit/Losses" between months over the entire period
total_net_change = sum(net_change_list)
total_average_change = (total_net_change)/(total_months)

##The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(net_change_list)

#The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(net_change_list)

##Print out the info
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: " + str(total_months))
print(f"Total: " + str(total_net_profit))
print(f"Average Change: " + str(total_average_change))
print(f"Greatest Increase in Profits: " + str(greatest_increase))
print(f"Greatest Decrease in Profits: " + str(greatest_decrease))

