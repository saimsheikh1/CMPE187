#Student: Saim Sheikh
#Date: 2/2/2023
#Course: CMPE 187
#Professor: Ishie Eswar
#Assignment Description:
#Gumball Vending Machine
# Design a Gumball Vending machine with the following specifications.
# Machine has two types of gumballs : Red and Yellow. Red ones are worth a nickel and Yellow ones a dime.
# Customer can insert only nickel, dimes or quarters as valid currency. Anything other than that is returned on the push of the dispenses lever.
# There are two levers Red and Yellow to dispense respective type of gumballs.
# Customer can insert multiple coins until he chooses to hit on the dispenser lever.
# Machine vends a single gumball at a time. 
# Customer can enter a quarter, choose to dispense two Red gumballs( by hitting the red gumball dispenser lever twice) and hit a "Return My Change" lever to receive the 15 cents in return.
# **Assume the machine holds unlimited gumballs and unlimited change of currency to return.
import sys

def main():
    coins = {               #dictionary
        "quarter" : 25,
        "dime" : 10,
        "nickel" : 5
    } 
    # Customer can insert only nickel, dimes or quarters as valid currency. Anything other than that is returned on the push of the dispenses lever.
    coinString = input("Insert a coin (Quarter/Dime/Nickel) OR Dispence: ")
    total=0
   
    while(coinString != "Dispence"):                # Customer can insert multiple coins until he chooses to hit on the dispenser lever.
        
        #if coinstring=="quarter" or coinstring ==Quarter
        if (coinString == "Quarter"):                     # quarter = 25
            print("Total coin value: ", list(coins.values())[0])
            total += 25
            print("Total: ", total)                     #Update total
        elif (coinString == "Dime"):                        # dime = 10
            print("Total coin value: ", list(coins.values())[1])
            total += 10
            print("Total: ", total)                       #Update total
        elif (coinString == "Nickel"):                      # nickel = 5
            print("Total coin value: ", list(coins.values())[2])
            total += 5
            print("Total: ", total)                       #Update total
                      
        coinString = input("Insert a coin (Quarter/Dime/Nickel) OR Dispence: ")         #loop until user enters Dispence
    
    
    while (total > 0):        #balance is not zero
        n = int(input("Enter 1 for RED Gumball\nEnter 2 for YELLOW Gumball\nEnter 3 To Return Change\nEnter:"))     #Display Levers
        if (n == 1):                                   #RED
            if(total>5):                        #Check if balance is greater than 5 cents
                total-=5                        #Yes, then deduct 5 cents
                print("\nDispenced Red Gumball\n")    #Dispence Red Gumball#
            else:                                     #No, then print Not enough balance
                print("Not enough balance")
                break    
        elif (n == 2):                               #yellow gumball is 10 cents or dime
            if(total>10):                      #Check if balance is greater than 10 cents
                total-=10
                print("\nDispenced Yellow Gumball\n")
            else:
                print("Not enough balance")
                break
        elif(n==3):                                 #Return Change
            print("\nChange Returned: ", total)  #Return balance
            break
        else:
            print("Invalid Input, enter 1, 2, or 3")
            
    print("Thank you for using the Gumball Vending Machine")
    sys.exit()
main()