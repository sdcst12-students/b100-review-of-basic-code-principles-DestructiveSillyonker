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
    


    while True:
        try:
            P = float(input("🤑🤑🤑🤑🤑 How many dollas do you have: "))
            R = float(input("what percentage will you 🤑🤑🤑 multiplication: "))
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
            T = float(input("🤑 how many times of time will yoiu time: "))
            T = T / Time 
            R = R / 100 
            Output = P * R * T
            print(Output)
            break
        except Exception as x:
            print("nuh uh", x)




if __name__ == "__main__":
    main()