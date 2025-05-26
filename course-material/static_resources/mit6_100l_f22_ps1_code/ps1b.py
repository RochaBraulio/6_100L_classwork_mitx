## 6.100A PSet 1: Part B
## Name: Braulio
## Time Spent: 16'
## Collaborators: None

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal (e.g. 0.1 for 10%): "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal (e.g. 0.1 for 10%): "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25 # assumes a down payment of 25%
amount_saved = 0 # assumes no amount previously saved for down payment
r = 0.05 # annual interest rate
A_total = cost_of_dream_home*portion_down_payment - amount_saved #effective down payment
initial_month_salary = yearly_salary/12

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

months = 0
A_current = amount_saved

while A_current <= A_total:
    monthly_salary = initial_month_salary*((1 + semi_annual_raise)**int(months/6))
    A_current = A_current*(1 + r/12) + monthly_salary*portion_saved
    months = months + 1

print(f'Number of months: {months}')