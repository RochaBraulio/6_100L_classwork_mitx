def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	return months