import os
import csv
import locale
import copy

budget = os.path.join("Resources","budget_data.csv")

date = []
profit =[]
months = 0
total_profit = 0
average = 0
increase = []
decrease = []
new_prof = []
average_p = 0
d_month = 0
d_index = []
i_month = 0


with open(budget, newline='') as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',') 
    csv_header = next(csvreader)

    for row in csvreader: 
        total_profit = total_profit + int(row[1])
        months = months + 1
        profit.append(int(row[1]))
        d_index.append(str(row[0]))

    for row in range(0,len(profit)-1):
        new_prof.append(profit[row+1]-profit[row])
 
    for row in range(0,len(new_prof)):
        average = average + new_prof[row]
    average = average/len(new_prof)

decrease = copy.copy(new_prof)
decrease.sort()
increase = decrease[len(decrease)-1]
d_new = d_index[new_prof.index(decrease[0])+1]
i_new = d_index[new_prof.index(increase)+1]


print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {months}")
print('Total: ${:0,.2f}'.format(total_profit).replace('$-','-$'))
print('Average Change: ${:0,.2f}'.format(average).replace('$-','-$'))
print('Greatest Increase in Profits: '+i_new +' ${:0,.2f}'.format(increase).replace('$-','-$'))
print('Greatest Decrease in Profits: '+d_new +' ${:0,.2f}'.format(decrease[0]).replace('$-','-$'))

results1 = "Financial Analysis"
results2 = "-------------------------"
results3 = f"Total Months: {months}"
results4 = 'Total: ${:0,.2f}'.format(total_profit).replace('$-','-$')
results5 = 'Average Change: ${:0,.2f}'.format(average).replace('$-','-$')
results6 = 'Greatest Increase in Profits: '+i_new +' ${:0,.2f}'.format(increase).replace('$-','-$')
results7 = 'Greatest Decrease in Profits: '+d_new +' ${:0,.2f}'.format(decrease[0]).replace('$-','-$')


output_file = os.path.join("analysis","PyBang_Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Months: {months}"])
    writer.writerow(['Total: ${:0,.2f}'.format(total_profit).replace('$-','-$')])
    writer.writerow(['Average Change: ${:0,.2f}'.format(average).replace('$-','-$')])
    writer.writerow(['Greatest Increase in Profits: '+i_new +' ${:0,.2f}'.format(increase).replace('$-','-$')])
    writer.writerow(['Greatest Decrease in Profits: '+d_new +' ${:0,.2f}'.format(decrease[0]).replace('$-','-$')])