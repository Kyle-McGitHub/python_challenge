import csv

bank_data = r"C:\Users\Kyle_McDaniel_Python\Desktop\Columbia_Analytics_Bootcamp\python_challenge\starter_code\pybank\resources\budget_data.csv"
results = r"C:\Users\Kyle_McDaniel_Python\Desktop\Columbia_Analytics_Bootcamp\python_challenge\starter_code\pybank\results.txt"

#this is part of the sum function
total_sum = 0

#variables
profit_loss_column = 1
profit_loss_column_values = 0
months = 0
dataset = []

with open(bank_data, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    
#sum all values in column B
#establishes line_count starting at "row" and then adds one, to eliminate the header

    for row in csvreader:
        profit_loss_value = int(row[profit_loss_column])
        dataset.append(profit_loss_value)

        months += 1
        profit_loss_column_values += profit_loss_value

biggest_increase = max(dataset)
biggest_decrease = min(dataset)

mean = profit_loss_column_values / months

print("Total Months:", months)
print("Total: $", profit_loss_column_values)
print("Mean: $", mean)
print("Greatest Increase in Profits: $", biggest_increase)
print("Greatest Decrease in Profits: $", biggest_decrease)

with open(results, 'w') as output:
    output.write("Total Months: {}\n".format(months))
    output.write("Total: $ {}\n".format(profit_loss_column_values))
    output.write("Mean: $ {}\n".format(mean))
    output.write("Greatest Increase in Profits: $ {}\n".format(biggest_increase))
    output.write("Greatest Decrease in Profits: $ {}\n".format(biggest_decrease))

print("Bank results have been written to results.txt!")