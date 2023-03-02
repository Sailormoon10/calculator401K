# This function tracks the number of biweekly checks  remaining in the calendar year.
# The calculator assumes that the first paycheck was issued on January 6th, 2023 [the first Friday of the year].
# Every 14 days equals 1 paycheck period.
# The function takes in 2 parameters: the first check date and today's date.
# Next, the function calculates how many days have passed and divides it by a biweekly schedule of 14 days.
# We use the int() function to ensure that a pay period is not counted unless the days passed is evenly divisible by 14.


def biweekly_check(first_check, today):
    days_passed = (today - first_check).days
    schedule = 14
    period = int(days_passed / schedule)
    return period


