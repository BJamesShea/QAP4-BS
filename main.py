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
            # Custome phone number
            phoneNum = input("Enter the customers phone number (###-###-####): ")
            if isValidName(phoneNum):
                break
            print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")

        # Returns
        return custFirstName, custLastName, custStrAdd, custCity, prov.upper(), postCode, phoneNum

    # Perform required calculations.
customerData = customerInfo()

    # Display results
    

# Any housekeeping duties at the end of the program