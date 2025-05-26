def part_c(initial_deposit):
	#########################################################################
	
	cost_of_dream_home = 800000
	down_payment = cost_of_dream_home*0.25
	months = 36
	steps_upper_limit = 1000 # allow to break from possible infinite while loop
	r_lower_limit = 0
	r_upper_limit = 1
	r = (r_lower_limit + r_upper_limit)/2 # initial guess for interest rate
	delta_down_payment_needed = 0
	amount_saved = 0
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	
	amount_saved = initial_deposit*((1 + r/12)**months)
	delta_down_payment_needed = amount_saved - down_payment #determines if the amount saved is sufficent or not
	
	if abs(delta_down_payment_needed) <= 100: #initial guess for interest rate was good enough
	    print(f'Best savings rate: {r} [or very close to this number]')
	    print(f'Steps in bisection search: {steps} [or very close to this number]')
	else:
	    while abs(delta_down_payment_needed) > 100:
	        if delta_down_payment_needed > 0:
	            #amount saved was greater than down payment required, lower interest rate
	            if steps > steps_upper_limit:
	                r = None
	                steps = 0
	                break
	            r_upper_limit = r
	            r = (r_lower_limit + r_upper_limit)/2
	            amount_saved = initial_deposit*((1 + r/12)**months)
	            steps = steps + 1
	            delta_down_payment_needed = amount_saved - down_payment
	        else:
	            #amount saved was lower than down payment required, interest rate must be higher
	            if steps > steps_upper_limit:
	                r = None
	                steps = 0
	                break
	            r_lower_limit = r
	            r = (r_lower_limit + r_upper_limit)/2
	            amount_saved = initial_deposit*((1 + r/12)**months)
	            steps = steps + 1
	            delta_down_payment_needed = amount_saved - down_payment
	
	print(f'Best savings rate: {r} [or very close to this number]')
	print(f'Steps in bisection search: {steps} [or very close to this number]')
	return r, steps