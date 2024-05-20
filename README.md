


## Development Notes 
new repository for this project: __customer_banking__

### __Accounts.py__ file contains the Account class with methods to set the balance and interest

https://bootcampspot.instructure.com/courses/6442/assignments/80409?module_item_id=1260685


# Main Function

## Create the Main Function
In __customer_banking.py__ file, you will 
+ import the __create_savings_account__ and __create_cd_account__ functions, 
+ then create a __main__ function that: 

### calling the savings_account
1. Prompt the user to set the __savings balance, interest rate, and months__ for the savings account. 

2. Call the __create_savings_account__ function and pass in the variables from the user:. (8 points)
   
3. Print out the interest earned and updated savings account balance with interest earned for the given months.

### calling the cd account
3.Prompt the user to set the __CD balance, interest rate, and months__ for the CD account. (8 points)

4. Call the __create_cd_account__ function and pass the variables to the function from the user.

5. Print out the interest earned and updated __CD account balance__ with __interest earned__ for the given months.

6. The main function is called to run the program. (2 points)



# Savings Account
Prompt the user to enter the savings account details: 
__savings balance, interest rate, and months__ for the savings account.

Call the __create_savings_account__ function and pass in the variables from the user.

Print out the __interest earned__ and __updated savings account__ balance with __interest earned__ for the given months. 

_The values are formatted to two decimal places and thousandths._

### Create the Savings Account Function (35 points)
In __savings_account.py__ you will:
1. The Account class from the Accounts.py file is imported. (4 points)

2. In the __create_savings_account__ function, an instance of the Account class is created and the __balance__ and __interest__ parameters are passed to the Account class. (6 points)

3. The interest earned is calculated and assigned to a variable. calculate the __interest earned__ based on user input :(4 points)
      +  _interest = balance * (apr/100 * months/12)_
 
4. The savings __account balance__ is updated by adding the __interest earned__ to the __balance__ and assigned to a variable. (4 points)
   
5. . The updated balance is passed to the __set balance__ method using the instance of the Account class. (6 points)

6.  The __interest earned__ is passed to the ?? _set_interest_ ? set balance ?method using the instance of the Account class. (6 points)

7.  return the __updated balance__ and __interest earned__. by the function. (5 points)


# CD Account
_Code is written to print out the interest earned and updated __CD account balance__ with __interest earned__ for the given months. 

Call the __create_cd_account__ function and pass the variables to the function used to prompt the user._

?? Prompt the user to set CD account details: 
the __CD balance, interest rate, and months__ for the CD account.

_The values are formatted to two decimal places and thousandths._
### Create the CD Account Function (35 points)
1. The Account class from the Accounts.py file is imported. (4 points)

2. In the __create_cd_account__ function, an instance of the Account class is created and the __balance__ and __interest__ parameters are passed to the Account class. (6 points)

3. calculate the __interest earned__ based on user input, (The interest earned is calculated and assigned to a variable.) (4 points)

4. The __CD account balance__ is updated by adding the __interest earned__ to the balance and assigned to a variable. (4 points)

5. The __updated balance__ is passed to the __set balance__ method using the instance of the Account class. (6 points)

The __interest earned__ is passed to the __set balance__ method using the instance of the Account class. (6 points)

The __updated balance__ and __interest earned__ are returned by the function. (5 points)