print("Track your loans and investments with our EXPENSE TRACKER")

p_amount = 0
rate = 0
time = 0

def r_rate():
    global rate
    if rate <=0 :
        raise ValueError("Enter a number greater than 0")
    return round(rate/100/12, 2)

def num():
    global time
    if time <=0 :
            raise ValueError("Enter a number greater than 0")
    return 12*time
def monthly_repayment(p_amount):
     r = r_rate()
     n = num()
     return round(
          (p_amount*(r*(1+r)**n))/((1+r)**n-1), 2)

def total_amount(p_amount):
      return round(monthly_repayment(p_amount) * num(), 2)
total_interest= lambda p_amount, total_amount: round(total_amount - p_amount, 2)
percentage = lambda total_interest, total_amount: round((total_interest/total_amount)*100, 2)

def loan_classifier(p_amount, interest):
     ratio = (interest/p_amount)*100

     if ratio < 20:
          return "Low interest"
     elif ratio <= 40:
          return "Moderate Interest"
     else:
          return "High Interest"


print("-"*40)
print("YOUR FINANCE SUMMARY")
print("-"*40)
while True:
    try:
        p_amount = float(input("Enter your principal amount: ").strip())
        rate = float(input("Enter your Annual Interest Rate: ").strip())
        time= float(input("Enter the term of your loan:  ").strip())
        total = total_amount(p_amount)
        interest = total_interest(p_amount, total)
        pct = percentage(interest, total)    
        print(f"Monthly Repayment: {monthly_repayment(p_amount)}")
        print(f"Total Amount: {total_amount(p_amount)}")
        print(f"Total Interest: {interest}")
        print(f"Percentage:{pct}%")

        print(f"Your loan is classified as: {loan_classifier(p_amount, interest)}")

    except ValueError as error:
     print(f"ERROR!!!{error}")  

    exit=input("Do you want to exit(y/n)")
    if exit.lower()!="n":
         print(".............")
         break






