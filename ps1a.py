annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_of_downpayment = 0.25
rate_of_return = 0.04
current_saving = 0
months = 0
downpayment = total_cost * portion_of_downpayment
monthly_saved = (annual_salary / 12) * portion_saved

while current_saving < downpayment:
    current_saving += (current_saving * rate_of_return / 12) + monthly_saved
    months += 1

print("Number of Months: " + str(months))
