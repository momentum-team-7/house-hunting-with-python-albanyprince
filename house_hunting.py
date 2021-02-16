
# portion_down_payment = 0.25

# annual_salary = 120000
# monthly_salary = 10000
# portion_saved = 10% (0.1)
# monthly_amount_saved = monthly_salary*portion_saved
# monthly_amount_saved + interest_earned
# (r is rate of return[interest earned])
# interest_earned = current_savings*.04/12
total_cost = int(input("What is the total cost of your dream home? " ))
annual_salary = int(input("What is your annual salary? "))
portion_saved = float(input("How much per month will you save? Write as a decimal. ") or "0.10 ") 
portion_down_pymt = float(input("What portion is your down payment ") or "0.25 ")
r = float(input("What is the rate of return ") or "0.04 ")    
down_pymt = 0

def months():
    months = 0
    current_savings = 0
    monthly_salary = annual_salary/12
    monthly_amount_saved = monthly_salary*portion_saved
    interest_earned = current_savings*r/12
    down_pymt = total_cost*portion_down_pymt
    
    while current_savings < down_pymt:
        current_savings += monthly_amount_saved + interest_earned
        months += 1

    print (f"You will need {months} month(s) to buy this home")    

months()
