# Date is automatically set up
from datetime import date

def calculator_401k():
    today = date.today()

    monthly = 12
    semimonthly = 24
    biweekly = 26
    weekly = 52

    current_month = today.month
    current_week = today.isocalendar()[1]
    # current_biweekly_period = 
    # current_semimonthly_period = 

    remaining_months = monthly - current_month
    remaining_weeks = weekly - current_week
    remaining_biweekly_period = biweekly - 4
#     semimonthly_period = semimonthly - 4

    def progress(frequency, goal, contribution):
        if frequency == "monthly":
            amount_needed = (goal - contribution) / remaining_months
        elif frequency == "biweekly":
            amount_needed = (goal - contribution) / remaining_biweekly_period
        else:
            amount_needed = (goal - contribution) / remaining_weeks
        print(f"You need to save ${amount_needed:.2f} {frequency} by the end of the year to max your 401k.")

    # Function: User enters their pay schedule [Weekly, Biweekly, Monthly]
    # calculates the remaining weeks/pay periods to reach goal
    # and shows user how much they need to save to reach their goal by December 31st.
    
    def pay_period(pay_schedule):
        pay_schedule.lower()
        if pay_schedule == "monthly":
            print(f'You have {remaining_months} months remaining to reach your 401k goal.')
        elif pay_schedule == "biweekly":
            print(f'You have {remaining_biweekly_period} pay periods remaining to reach your 401k goal.')
        else:
            print(f"You have {remaining_weeks} weeks remaining to reach your 401k goal.")

    # User enters retirement goal for the year
    goal = int(input("How much do you want to contribute to your 401k by the end of the year? $"))

    # User enters amount of their current cash contributions [exclude any investment gains]
    contribution = float(input("\nEnter the amount you have saved,\n[Exclude gains or employer match]: $"))

    User enters their pay schedule [Weekly, Biweekly, Monthly]
    pay_frequency = input("\nEnter how often you get paid (monthly, biweekly, weekly): ")
    pay_period(pay_frequency)
    progress(pay_frequency, goal, contribution)


calculator_401k()
