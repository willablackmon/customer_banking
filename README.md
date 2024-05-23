

## Customer Banking Application  


__Accounts.py__ file contains the Account class with methods to set the balance and interest

### Main Function
+ __customer_banking.py__ serves as driver and launches function main to start this application.  

+ The user is prompted for for inputs: __balance, interest rate, and months__ 
for the savings account and cd account.  (Both of these functions must be imported
into customer_banking.py).

### Calling Sub Functions
+ User input values are passed into the __create_savings_account__ and __create_cd_account__
functions (in __savings_account.py*__ and __create_cd_account__ in __cd_account.py*__).  

*Both of these files require the Account class from Account.py to be imported.

+ __interest earned__ and __updated account balance__ are calculated in the savings and cd account, 
based on the user inputs.
>     interest = balance * (apr/100 * months/12)
  
+ These values are passed to the Account ojects created in each function using __Account class__ instances created and Account class member functions __set_interest__ and __set balance__.  

+ The functions return the __updated account balance__ and __interest earned__ to customer_banking.py
where the outputs are formatted and printed out for the user.



## Development Notes 
new repository project: __customer_banking__

https://bootcampspot.instructure.com/courses/6442/assignments/80409?module_item_id=1260685
