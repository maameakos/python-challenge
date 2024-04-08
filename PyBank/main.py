# Author Mina Agyen
import csv
# Function that analyzes the records to calculate certain amalytical values
def financial_analysis(data):
    total_num_months = len(data)
    net_profit_losses = sum(int(row[1]) for row in data)
    profit_losses_changes = [int(data[i][1]) - int(data[i-1][1]) for i in range(1, len(data))]
    average_change = sum(profit_losses_changes) / len(profit_losses_changes)
    greatest_increase = max(profit_losses_changes)
    greatest_decrease = min(profit_losses_changes)
    greatest_increase_index = profit_losses_changes.index(greatest_increase) + 1
    greatest_decrease_index = profit_losses_changes.index(greatest_decrease) + 1
    greatest_increase_date = data[greatest_increase_index][0]
    greatest_decrease_date = data[greatest_decrease_index][0]

    return (total_num_months, net_profit_losses, average_change,
            greatest_increase_date, greatest_increase,
            greatest_decrease_date, greatest_decrease)

# Read budget data from CSV
with open('Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    financial_data = list(reader)

total_num_months, net_profit_losses, average_change, greatest_increase_date, greatest_increase, greatest_decrease_date, greatest_decrease = financial_analysis(financial_data)

# Print results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_num_months))
print("Total: $" + str(net_profit_losses))
print("Average Change: $" + str(round(average_change,2)))
print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")")

# Writing results to a text file
with open('analysis/analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------------\n")
    output_file.write("Total Months: " + str(total_num_months)+ "\n")
    output_file.write("Total: $" + str(net_profit_losses) +"\n")
    output_file.write("Average Change: $" + str(round(average_change,2))+"\n")
    output_file.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")"+"\n")
    output_file.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")"+"\n")

