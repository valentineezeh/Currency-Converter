#CurrencyConverter.py
#Scripted By: Ugochukwu Ezeh
# Description: Converts USD to Naira and Vice Versa.

#1USD = 314.7500NGN
#1NGN = 0.003177USD

def CurrencyConverter():
    #Find out what the user wants to convert. 1) USD -> NGN or 2) NGN -> USD
    #Store answer into a variable
    print ("-----------------------------------------------------------")
    user_choice = input ("What do you want to convert? \n1) USD > NGN:  \n2) NGN > USD: \n")
        
    # Check and see what the user typed.
 
    #if the user type 1
    if user_choice == "1":
        #Promote the user the amount of USD they want to convert to NGN
        #Store the user input into a variable
        user_usd = input("Enter the amount in USD that you wish to convert: ")
        ngn = user_usd * 314.7500
        #output amount to user
        print ("".join("%sUSD = %sNGN" %(user_usd, ngn)))
        print ("---------------------------------------------------------------")
        do_again()
        
    #if the user typed 2
    elif user_choice == "2": 
        #Promote the user the amount of NGN they want to convert to USD
        #Store the user input into a variable
        user_ngn = input("Enter the amount in NGN that you wish to convert: ")
        usd = user_ngn * 0.003177
        #USD = NGN amount * 314.7500
        #output amount to user
        print ("".join("%sNGN = %sUSD" %(user_ngn, usd)))
        print ("-----------------------------------------------------------")
        do_again()
    #if the user type anything else
    else:
        #Tell the user what they did wrong
        print ("Error: You enter an invalid information, please try again.")
        print ("------------------------------------------------------------")
        #Run the script again
        CurrencyConverter()

def do_again():
    #This promote the user if they want to run the Currency Converter again.
    user_do_again = input("Would you like to run this app again \n1) Yes \n2) No \n")
    if user_do_again == "1":
        CurrencyConverter()
    elif user_do_again == "2":
        print ("Thank you for using this program..")
    else:
        print ("Error: You enter an invalid information, please try again.")
        do_again()
CurrencyConverter()