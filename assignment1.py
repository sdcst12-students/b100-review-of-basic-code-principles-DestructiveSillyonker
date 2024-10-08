"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""
def main():
  P = input("How many dollas do you have: ")
  R = input("what percentage will you multiplication: ")
  while True:
    Time = input("Months, Days, Years (M/D/Y): ")
    if Time == 'M':
      Time = 12
      break
    elif Time == 'D':
      Time = 365
      break
    elif Time == 'Y':
      Time = 1
      break




if __name__ == "__main__":
  ...