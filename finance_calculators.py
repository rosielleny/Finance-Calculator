import math

print("""\nChoose either 'investment' or 'bond' from the menu below to proceed:
    \ninvestment – to calculate the amount of interest you'll earn on your investment 
    \nbond – to calculate the amount you'll have to pay on a home loan""")

choice_bool = False # These establish the variables for all while loops.
deposit_bool = False
interest_rate_bool = False
years_bool = False
interest_bool = False
house_bool = False
interest_bon_bool = False
months_bool = False

while choice_bool is False: # This while loop ensures that if the user inputs an invalid choice, the program will return to the start after printing the error message and prompt for their choice again instead of stopping.
    choice = input("\nEnter choice here: ")
    
    if choice == "investment" or choice == "INVESTMENT" or choice == "Investment": # Ensures any of these forms of 'investment' will be accepted.
        choice_bool = True # Exits the while loop as the user has entered their choice correctly.
        
        while deposit_bool is False: # This while loop, and those following for each variable requiring user input, ensures the user enters a number and prompts for input again if they haven't, thus preventing the program from stopping in the event a number isn't entered.
            deposit = input("\nPlease enter the amount of money you are depositing. £")
            try: 
                deposit = float(deposit)
                deposit_bool = True
            except:
                print("\nError: Please enter a number or decimal only.")
        
        while interest_rate_bool is False: # This while loop ensures the user enters a number and prompts for input again if they haven't, thus preventing the program from stopping in the event a number isn't entered.
            interest_rate = input("\nPlease enter the anual interest rate in percent. ")
            if "%" in interest_rate: # This conidition removes an added % sign as it seems the most likely user error. This saves having to specify this, and saves user frustration.
                interest_rate = interest_rate.replace("%","")
            try:
                interest_rate = float(interest_rate)
                interest_rate_bool = True
            except:
                print("\nError: Please enter a number or decimal only.")
       
        while years_bool is False: # This while loop ensures the user enters a number and prompts for input again if they haven't, thus preventing the program from stopping in the event a number isn't entered.
            years = input("\nPlease enter the number of years you plan to invest for (numbers and/or decimals only). ")
            try:
                years = float(years)
                years_bool = True
            except:
                print("\nError: Please enter a number or decimal only.")
                  
        while interest_bool is False: # This while loop ensures the user enters a valid option and prompts for input again if they haven't, thus preventing the program from stopping in the event a valid option isn't entered.
            interest = input("\nWould you like simple interest or compound interest? ")
           
            if "simple" in interest or "SIMPLE" in interest or "Simple" in interest:
               
                total_amount = deposit*(1+(interest_rate/100)*years) # Calculates simple interest.
                interest_earned = round((total_amount - deposit), 2)
                interest_bool = True # Exits the interest_bool while loop as the user has entered their choice correctly.
           
            elif "compound" in interest or "COMPOUND" in interest or "Compound" in interest:
                
                total_amount = round(deposit* math.pow((1+(interest_rate/100)),years), 2) # Calculates compound interest.
                interest_earned = round((total_amount - deposit), 2)
                interest_bool = True # Exits the interest_bool while loop as the user has entered their choice correctly.
            
            else:
                print("\nError: Please enter a valid choice by typing 'simple' or 'compound'.") 
        
        print(f"\nThe total interest you will earn after {years} years will be £{interest_earned}, giving you £{total_amount} in total.") # Prints the final answer, ending the program.
   
    elif choice == "bond" or choice == "BOND" or choice == "Bond":
        
        choice_bool = True # Exits the while loop as the user has entered their choice correctly.
        
        while house_bool is False: # This while loop ensures the user enters a number and prompts for input again if they haven't, thus preventing the program from stopping in the event a number isn't entered.
            house_value = input("\nPlease enter the present value of the relevant house (numbers only, no commas). £")
            try:
                house_value = float(house_value)
                house_bool = True
            except:
                print("\nError: Please enter a number or decimal only.")

        while interest_bon_bool is False: # This while loop ensures the user enters a number and prompts for input again if they haven't, thus preventing the program from stopping in the event a number isn't entered.
            interest_bon = input("\nPlease enter the anual interest rate in percent. ")
            if "%" in interest_bon: # This conidition removes an added % sign as it seems the most likely user error. This saves having to specify this, and saves user frustration. 
                interest_bon = interest_bon.replace("%","")
            try:
                interest_bon = float(interest_bon)
                interest_bon_bool = True
            except:
                print("\nError: Please enter a number or decimal only.")

        while months_bool is False: # This while loop ensures the user enters a number and prompts for input again if they haven't, thus preventing the program from stopping in the event a number isn't entered.
            months = input("\nPlease enter the number of months you plan to take to repay the bond (numbers and/or decimals only). ")
            try:
                months = float(months)
                months_bool = True
            except:
                print("\nError: Please enter a number or decimal only.")
        repayment = round((((interest_bon/100)/12) * (1/(1-(1+(interest_bon/100)/12)**(-months)))*house_value), 2) # Calculates bond repayment.
        
        print(f"\nThe amount you will have to repay each month is £{repayment}.") #Prints the final answer, ending the program.
    
    else:
        print("\nError: please enter a valid choice by typing 'investment' or 'bond'.")