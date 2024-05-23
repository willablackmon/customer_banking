from cd_account import create_cd_account 
from savings_account import create_savings_account 


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
# Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance, savings_interest, savings_maturity = input(
'''\nPlease enter your current Savings Account Balance ($), Interest Rate (%), and Maturity (Months), 
separated by a blank space >>  ''').split()
    
    # print(f'You entered Savings Account Balance: ${savings_balance}, Int. Rate: {savings_interest}%, and Maturity: {savings_maturity} months.')
    
# Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, sav_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

# Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'''\tYour Savings Account balance is now: ${updated_savings_balance: .2f}
\tYour Savings Account has earned ${sav_interest_earned: .3f} in interest in the last {savings_maturity} months.''')

# Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance, cd_interest, cd_maturity = input(
'''\nPlease enter your current CD Balance ($), Interest Rate (%), and Maturity (Months), 
separated by a blank space >>  ''').split()

# Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

# Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'''\tYour CD balance is now: ${cd_updated_balance: .2f}.  
\tYour CD has earned ${cd_interest_earned: .3f} in interest in the last {cd_maturity} months.''')
    
if __name__ == "__main__":
# Call the main function.
    main()