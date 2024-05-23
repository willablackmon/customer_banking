from Account import Account 


def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
# Create an instance of the `Account` class and pass in the balance and interest parameters.
    cd_acct = Account(balance, interest_rate)

# Calculate interest earned
    interest_earned = 0
    interest_earned = float(balance) * (float(interest_rate)/100 * int(months)/12)
# Update the CD account balance by adding the interest earned
    updated_balance = 0
    updated_balance = float(balance) + interest_earned

# Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_acct.set_balance(updated_balance)

# Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_acct.set_interest(interest_earned)

# Return the updated balance and interest earned.
    return updated_balance, interest_earned  