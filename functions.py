# funkytown functions
def isValidName(name):
    ALLOWED_CHAR_SET = set("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-. '1234567890")
    return set(name).issubset(ALLOWED_CHAR_SET)

def isValidNum(name):
    ALLOWED_NUM_SET = set("1234567890-")
    return set(name).issubset(ALLOWED_NUM_SET)


def customerInfo():
    while True:
        # Customer first name
        custFirstName = input("Enter the customers first name (Type End to end program.): ").title()
        if custFirstName == "End":
            exit()
        elif isValidName(custFirstName):
            break
        print("Error - Please only use letters, numbers, hyphens, apostrophes, and/or periods.")
    
    while True:
        # Customer last name
        custLastName = input("Enter the customers last name: ").title()
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
        custCity = input("Enter the customer city: ").title()
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
        if isValidNum(phoneNum):
            break
        print("Error - Please only use numbers.")

    # Returns
    return custFirstName.title(), custLastName.title(), custStrAdd, custCity.title(), prov.upper(), postCode.upper(), phoneNum

def vehicleInfo():
    while True:
        # Number of cars being insured
        numCars = input("Enter the amount of cars to be insured (Type End to end program). ")
        if numCars == "End":
            exit()
        elif numCars.isdigit():
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
    return numCars, extraLiab.upper(), glassCoverage.upper(), loanerCar.upper()


def paymentInfo():
    downPayment = 0
    paymentMethodLst = ["Full", "Monthly", "Down Payment"]
    while True:
        # Paying in monthly or full amount
        paymentMethod = input("How would the customer like to pay? (Full, Monthly, or Down payment.): ").title()
        if paymentMethod not in paymentMethodLst:
            print("Error - Invalid payment type.")
        elif paymentMethod == "Down Payment":
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


def claimInfo():
    while True:
        # Claim number
        claimNum = input("Enter the claim number. (Type End to end program) ")
        if claimNum == "End":
            exit()
        elif claimNum.isdigit():
            claimNum = int(claimNum)
            break
        print("Error - Please enter a numeric value.")

    while True:
        # Claim date
        claimDate = input("Please enter the claim date (YYYY-MM-DD): ")
        if isValidNum(claimDate):
            break
        print("Error - Please only use numbers.")

  
    # Returns
    return claimNum, claimDate,

import datetime

def prevClaimInfo():
    prevClaimLst = []

    while True:
        previousClaim = input("Does this customer have any previous claims? (Y for yes / N for no): ").upper()
        if previousClaim == "N":
            break
        elif previousClaim != "Y":
            print("Please enter Y or N.")
            continue

        previousClaimNumber = input("Please enter the previous claim number: ")
        if not isValidNum(previousClaimNumber):
            print("Error - Please only use numbers.")
            continue

        previousClaimDate = input("Please enter the previous claim date (YYYY-MM-DD): ")
        try:
            previousClaimDate = datetime.datetime.strptime(previousClaimDate, "%Y-%m-%d").date()
        except ValueError:
            print("Error - Invalid date format. Please use YYYY-MM-DD.")
            continue

        previousClaimAmount = input("Please enter the previous claim amount: ")
        if not isValidNum(previousClaimAmount):
            print("Error - Please only use numbers.")
            continue

        prevClaimLst.append((previousClaimNumber, previousClaimDate, previousClaimAmount))

    return prevClaimLst

def continueProgram():
    while True:
        continueProg = input("Would you like to continue this program? (Y/N): ").upper()
        if continueProg == "N":
            exit()
        elif continueProg == "Y":
            break
        else:
            print("Error - Please enter Y or N.")

    return continueProg