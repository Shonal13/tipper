"""
This program is used to calculate the tip using predefined tip values

Program flow is as follows:

1. User inputs Total Bill amount
2. User choose the tip amount from pre-defined tip range
3. No of people to split the bill
4. Outputs the bill amount to be paid by each person

"""

def tip_calc():

    print("Hello Human ! Welcome to this Tip Calculator !")
    print()

    total_bill = float(input("Please enter the total bill human : $"))

    tip_range  = int(input("Please select the percentage of amount you would like to tip ? 10% 12% or 15% ? "))

    split_people = int(input("With how many people would you like to split the bill ? "))

    ac_amount = (total_bill + (total_bill * tip_range/100))

    each_amount = (ac_amount / split_people)

    print(f"Each of you humans should pay : ${round(each_amount, 2)} ")

tip_calc()
