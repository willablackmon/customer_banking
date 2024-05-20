# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

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
'''Please enter your current Savings Account Balance ($), Interest Rate (%), and 
Maturity (Months), separated by a blank space:\n>>''').split()
    
    print(f'''You have entered Savings Account Balance: ${savings_balance}; 
Interest Rate {savings_interest}%; and Maturity: {savings_maturity} months.''')
    
# Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, sav_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

# Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'''In the last {savings_maturity} months your Savings Account has
earned the following interest: ${sav_interest_earned}/n.
Your Savings Account balance is now: ${updated_savings_balance}''')

# Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance, cd_interest, cd_maturity = input(
'''Please enter your current CD Balance ($), Interest Rate (%), and 
Maturity (Months), separated by a blank space:\n>>''').split()

    print(f'''In the last {savings_maturity} months your Savings Account has
earned the following interest: ${sav_interest_earned}/n.
Your Savings Account balance is now: ${updated_savings_balance}''')
    
# Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

# Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'''In the last {cd_maturity} months your CD has
earned the following interest: ${cd_interest_earned}/n.
Your CD balance is now: ${updated_cd_balance}''')
    


if __name__ == "__main__":
# Call the main function.
    main()

