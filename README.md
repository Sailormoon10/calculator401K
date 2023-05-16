# 401k Calculator

This Python script provides a simple 401k calculator to help users determine how much they need to save to reach their retirement goal by the end of the year. It takes into account the user's pay schedule and current contributions to provide personalized savings recommendations.

## Usage

To run the program, ensure that you have Python installed on your system. Save the code in a file with a `.py` extension, such as `401k_calculator.py`. Open a terminal or command prompt, navigate to the directory where the file is saved, and execute the following command:

```shell
python 401k_calculator.py
```

The program will prompt you to enter the necessary information, such as your retirement goal, current contributions, and pay schedule. Based on this information, it will calculate the remaining time and the amount you need to save to reach your goal by December 31st.

## Code Explanation

The code begins by importing the necessary modules, including `date` from `datetime`, `semimonthly_schedule`, and `biweekly_schedule`.

The script defines several functions and variables:

1. `calculator_401k()` function:
   - This function serves as the main entry point of the program.
   - It sets up the start date and retrieves the current day, week, and month.
   - It assigns the total number of checks for each pay schedule.
   - It determines the current pay period number for the semimonthly and biweekly pay schedules.
   - It calculates the remaining amount of checks for each pay schedule.
   - It defines the `progress()` function, which calculates the amount needed to save based on the current contributions and remaining time.
   - It defines the `pay_period()` function, which informs the user about the remaining pay periods or weeks based on their chosen pay schedule.
   - It prompts the user to enter their retirement goal, current contributions, and pay schedule.
   - It calls the `pay_period()` and `progress()` functions to display the recommended savings amount.

2. `pay_period(pay_schedule)` function:
   - This function takes the pay schedule as input and displays the remaining pay periods or weeks based on the chosen schedule.

3. `progress(frequency, goal, contribution)` function:
   - This function takes the pay frequency, retirement goal, and current contribution as inputs.
   - It calculates the amount needed to save based on the current contributions and remaining time.

## Example Usage

```shell
How much do you want to contribute to your 401k by the end of the year? $20000

Enter the amount you have saved,
[Exclude gains or employer match]: $5000

Enter how often you get paid (monthly, semimonthly, biweekly, weekly): monthly
You have 5 months remaining to reach your 401k goal.
You need to save $3000.00 monthly by the end of the year to max your 401k.
```

In the above example, the user wants to contribute $20,000 to their 401k by the end of the year. They have already saved $5,000 and receive monthly paychecks. The program informs them that they have 5 months remaining to reach their 401k goal and recommends saving $3,000 per month to max their 401k by the end of the year.

Feel free to enter your own values when prompted to get personalized savings recommendations.
