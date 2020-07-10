salary = int(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_of_downpayment = 0.25
rate_of_return = 0.04
current_saving = 0
months = 36
epsilon = 100
num_guesses = 0
low = 0
high = 10000
downpayment = total_cost * portion_of_downpayment
portion_saved = (low + high)/20000.0
#monthly_saved = (annual_salary / 12) * portion_saved


while abs(current_saving - downpayment) >= epsilon:
#    print(portion_saved)
    if abs(low - high) < 1:
        break
    current_saving = 0
    annual_salary = salary
    monthly_saved = (annual_salary / 12) * portion_saved
    for i in range(1,37):
        current_saving += (current_saving * rate_of_return / 12.0) + monthly_saved
        if i % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_saved = (annual_salary / 12.0) * portion_saved
#    print(current_saving)
    if current_saving < downpayment:
        low = int(portion_saved * 10000)
    else:
        high = int(portion_saved * 10000)
    portion_saved = (low + high)/20000.0
    num_guesses += 1
#    print(low, " ", high)

if abs(current_saving - downpayment) < epsilon:
    print("Best saving rate: " + str(portion_saved))
    print("Steps in bisection search: " + str(num_guesses))
else:
    print("It is not possible to pay the down payment in three years.")
