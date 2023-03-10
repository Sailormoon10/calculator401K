# Date is automatically set up
from datetime import date
import semimonthly_schedule
import biweekly_schedule

# Use datetime and isocalender functions to retrieve the first paycheck date, and today's day, week, and month.

def calculator_401k():
    start_date = date(2023, 1, 6)
    today = date.today()
    current_day = today.today().day
    current_week = today.isocalendar()[1]
    current_month = today.month
    
# Assign the total number of checks that the user will receive in a calendar year according to their pay schedule.
    monthly = 12
    semimonthly = 24
    biweekly = 26
    weekly = 52

# Determine the current pay period number for the semimonthly and biweekly pay schedule.

    current_biweekly_period = biweekly_schedule.biweekly_check(start_date, today)
    semimonthly_period = semimonthly_schedule.paycheck(current_month, current_day)

# Determine the remaining amount of checks for each pay schedule.

    remaining_months = monthly - current_month
    remaining_semimonthly_period = semimonthly - semimonthly_period
    remaining_biweekly_period = biweekly - current_biweekly_period
    remaining_weeks = weekly - current_week

# Calculate the amount you need to save depending on current contributions.
    def progress(frequency, goal, contribution):
        if frequency == "monthly":
            amount_needed = (goal - contribution) / remaining_months
        elif frequency == "semimonthly":
            amount_needed = (goal - contribution) / remaining_semimonthly_period
        elif frequency == "biweekly":
            amount_needed = (goal - contribution) / remaining_biweekly_period
        elif frequency == "weekly":
            amount_needed = (goal - contribution) / remaining_weeks
        print(f'You need to save ${amount_needed:.2f} {frequency} by the end of the year to max your 401k.')

    # Function: User enters their pay schedule [Weekly, Biweekly, Monthly]
    # calculates the remaining weeks/pay periods to reach goal
    # and shows user how much they need to save to reach their goal by December 31st.
    def pay_period(pay_schedule):
        pay_schedule.lower()
        if pay_schedule == "monthly":
            print(f'You have {remaining_months} months remaining to reach your 401k goal.')
        elif pay_schedule == "semimonthly":
            print(f'You have {remaining_semimonthly_period} pay periods remaining to reach your 401k goal.')
        elif pay_schedule == "biweekly":
            print(f'You have {remaining_biweekly_period} pay periods remaining to reach your 401k goal.')
        else:
            print(f"You have {remaining_weeks} weeks remaining to reach your 401k goal.")

    # User enters retirement goal for the year.
    goal = int(input("How much do you want to contribute to your 401k by the end of the year? $"))

    # User enters amount of their current cash contributions [exclude any investment gains]
    contribution = float(input("\nEnter the amount you have saved,\n[Exclude gains or employer match]: $"))

    # User enters their pay schedule [Weekly, Biweekly, Monthly, Semimonthly]
    pay_frequency = input("\nEnter how often you get paid (monthly, semimonthly, biweekly, weekly): ")
    pay_period(pay_frequency)
    progress(pay_frequency, goal, contribution)


calculator_401k()

