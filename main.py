# Description: QAP# 4 - One stop Insruance Company
# Author: Brandon Shea
# Date(s): March 14th 2024 - 

# Define required libraries.
import FormatValues as FV
import datetime
import sys
import time

# Define program constants.
f = open('def.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_DISCOUNT = float(f.readline())
EXTRA_LIAB_COV = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE = float(f.readline())
f.close()

curDate = datetime.datetime.now()

# Define program functions.


# Main program starts here.
       
# Gather user inputs.

def isValidName(name):
        ALLOWED_CHAR_SET = set("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-.'1234567890 ")
        return set(name).issubset(ALLOWED_CHAR_SET)


def customerInfo():
        while True:
            # Customer first name
            custFirstName = input("Enter the customers first name: ")
            if isValidName(custFirstName):
                break
            print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")
        
        while True:
            # Customer last name
            custLastName = input("Enter the customers last name: ")
            if isValidName(custLastName):
                break
            print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")

        while True:
            # Customer address
            custStrAdd = input("Enter the customers street address: ")
            if isValidName(custStrAdd):
                break
            print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")

        while True:
            # Customer city
            custCity = input("Enter the customer city: ")
            if isValidName(custCity):
                 break
            print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")

        provLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "SK", "NV"] # Province list
        while True:
            # Customer province
            prov = input("Enter the customer province (XX): ")
            if len(prov) != 2:
                print("Error - Must be two characters only")
            elif isValidName(prov):
                 break
            
            elif prov not in provLst:
                print("Error - Invalid Province")
            else:
                break

        while True:
            # Customer postal code
            postCode = input("Enter the customers postal code: ")
            if isValidName(postCode):
                break
            print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")

        while True:
            # Customer phone number
            phoneNum = input("Enter the customers phone number (###-###-####): ")
            if isValidName(phoneNum):
                break
            print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")

        # Returns
        return custFirstName, custLastName, custStrAdd, custCity, prov.upper(), postCode, phoneNum

def vehicleInfo():
        while True:
            # Number of cars being insured
            numCars = input("Enter the amount of cars to be insured. ")
            if numCars.isdigit():
                numCars = int(numCars)
                break
            print("Error - Please enter a valid number.")

        while True:
            # Extra Liability Coverage
            extraLiab = input("Does the customer want Extra Liability Coverage? (Y for yes / N for no): ").upper()
            if extraLiab in ["Y", "N"]:
                break
            print("Please enter Y or N.")
            
        if extraLiab == "Y":
             print("Customer has opted for Extra Liability Coverage!")
        else:
            print("Customer has opted not to have Extra Liability Coverage.")

        while True:
            # Optional Glass Coverage
            glassCoverage = input("Does the customer want Optional Glass Coverage? (Y for yes / N for no): ").upper()
            if glassCoverage in ["Y", "N"]:
                break
            print("Please enter Y or N.")

        if glassCoverage == "Y":
             print("Customer has opted for Optional Glass Coverage!")
        else:
            print("Customer has opted not to have Optional Glass Coverage.")


        while True:
            # Optional Loaner Car
            loanerCar = input("Does the customer want a Loaner Car? (Y for yes / N for no): ").upper()
            if loanerCar in ["Y", "N"]:
                break
            print("Please enter Y or N.")

        if loanerCar == "Y":
             print("Customer has opted for a Loaner Car!")
        else:
            print("Customer has opted not to have a Loaner Car.")

            # Returns
        return numCars, extraLiab, glassCoverage, loanerCar


def paymentInfo():
        paymentMethodLst = ["Full", "Monthly", "Down Pay"]
        while True:
            # Paying in monthly or full amount
            paymentMethod = input("How would the customer like to pay? (Full, Monthly, or Down pay.): ").title()
            if paymentMethod not in paymentMethodLst:
                print("Error - Invalid payment type.")
            elif paymentMethod == "Down Pay":
                while True:
                    downPaymentStr = input("How much would the customer like to put down as a down payment? ")
                    try:
                        downPayment = float(downPaymentStr)
                        break
                    except ValueError:
                        print("Error - Please enter a valid numerical value.")
                break
            else:
                break
        return paymentMethod, downPayment



    # Perform required calculations.









# Gather inputs
while True:
    customerData = customerInfo()
    insuranceInfo = vehicleInfo()
    paymentInformation = paymentInfo()

    # Display results
    

# Any housekeeping duties at the end of the program