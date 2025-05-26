def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	
	portion_down_payment = 0.25 # assumes a down payment of 25%
	amount_saved = 0 # assumes no amount previously saved for down payment
	r = 0.05 # annual interest rate
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	import math
	
	
	# Formula is available here
	# https://extrudesign.com/engineering-calculators/compound-interest-calculator/
	
	A = cost_of_dream_home * portion_down_payment - amount_saved #effective down payment
	Q = yearly_salary * portion_saved / 12 # recurring monthly deposits
	
	alpha = ((A * r) / (12 * Q) + 1)
	beta = 1 + r / 12
	
	years = math.log(alpha) / (12 * math.log(beta)) # number of years needed to reach A
	months = math.ceil(years * 12) # number of months needed to reach A
	
	print(f'Number of months: {months}')
	return months