import math
#financial calculator
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#investment calculator
if user_choice == "investment".lower():
    deposit = float(input("Enter the amount of money that you are depositing: "))
    investment_interest_rate = float(input("Enter the interest rate (as a percentage): "))
    investment_rate = float(investment_interest_rate/100)
    years = float(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter either 'simple' or 'compound' for the interest you want: ")

#simple interest
    if interest_type == "simple":
        amount = deposit * (1 + (investment_rate * years))
        amount2 = float("%.2f" % amount)
        print(f"Total amount of money you will earn is £{amount2}.")

#compound interest
    elif interest_type == "compound":
        amount_compound = deposit * math.pow((1 + investment_rate), years)
        amount_compound2 = float("%.2f" % amount_compound)
        print(f"Total amount of money you will earn is £{amount_compound2}.")

#user does not type in a valid input
    else:
        print("Invalid choice entered.")

#bond calculator
elif user_choice == "bond".lower():
    house_value = float(input("Enter the present vaule of your house: "))
    bond_interest_rate = float(input("Enter the interst rate (as a percentage): "))
    bond_rate = float((bond_interest_rate/12)/100)
    replayment_time = float(input("Enter the number of months you plan to repay the bond: "))
    repayment_amount = (bond_rate * house_value)/(1 - (1 + bond_rate)**(- replayment_time))
    repayment_amount2 = float("%.2f" % repayment_amount)
    print(f"You will need to repay £{repayment_amount2} monthly.")

#user does not type in a valid input
else:
    print("Invalid choice entered.")