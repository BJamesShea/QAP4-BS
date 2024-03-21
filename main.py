# Description: QAP# 4 - One stop Insruance Company
# Author: Brandon Shea
# Date(s): March 14th 2024 - March 20 2024

# Define required libraries.
import FormatValues as FV
import datetime
import sys
import time
import functions as FUN


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

while True:
  

    curDate = datetime.datetime.now()

    # Define program functions.

    # Main program starts here.
        
    # Gather user inputs.
    
        # Perform required calculations and initialize variables.
    
    finalCost = 0
    while True:
        customerData = FUN.customerInfo()
        insuranceInformation = FUN.vehicleInfo()
        paymentInformation = FUN.paymentInfo()
        claimInformation = FUN.claimInfo()
        prevClaimLst = FUN.prevClaimInfo()
        # previousClaimInformation = FUN.prevClaimInfo()

        custFirstName, custLastName, custStrAdd, custCity, prov, postCode, phoneNum   = customerData
        numCars, extraLiab, glassCoverage, loanerCar = insuranceInformation
        paymentMethod, downPayment = paymentInformation
        claimNum, claimDate, = claimInformation
        # prevClaimLst = previousClaimInformation

        
        

        if numCars == 1:
            insurancePremium = BASIC_PREM
        elif numCars > 1:
            insurancePremium = BASIC_PREM * ADD_DISCOUNT

        if extraLiab == "Y":
            extraLiabilityCost = EXTRA_LIAB_COV * numCars
        else:
            extraLiabilityCost = 0

        if glassCoverage == "Y":
            glassCoverageCost = GLASS_COV * numCars
        else:
            glassCoverageCost = 0

        if loanerCar == "Y":
            loanerCarCost = LOANER_CAR * numCars
        else:
            loanerCarCost = 0

        totalExtraCost = extraLiabilityCost + glassCoverageCost + loanerCarCost

        totalInsurancePremium = BASIC_PREM + totalExtraCost

        HST = totalInsurancePremium * HST_RATE

        finalCost = totalInsurancePremium + HST

        if paymentMethod == "Down Payment":
            monthlyPayment = (finalCost - downPayment + PROC_FEE) / 8
        else:
            monthlyPayment = (finalCost + PROC_FEE) / 8


    


        # DSPs conversions
        customerName = custFirstName + " " + custLastName
        invoiceDate = datetime.date.today()

        # Convert claim date to a date object
        claimDate = datetime.datetime.strptime(claimDate, "%Y-%m-%d").date()
        
        # First of next month
        nextMonth = invoiceDate.month + 1
        year = invoiceDate.year

        if nextMonth == 13:
            nextMonth = 1
            year += 1
        
        firstPaymentDate = datetime.date(year, nextMonth, 1)
        







        # Display results to the user.
        print()
        print("----------------------------------------------")
        print("----------ONE STOP INSURANCE COMPANY----------")
        print("----------------------------------------------")
        print()
        print("             CUSTOMER INFORMATION             ")
        print()
        print("----------------------------------------------")
        print(f"Customer Name:       {customerName:<20s}       ")
        print(f"Address:             {custStrAdd:<20s}         ")
        print(f"City:                {custCity:<14s}           ")
        print(f"Province:            {prov:<2s}                ")
        print(f"Postal Code:         {postCode:<6s}            ")
        print(f"Phone Number:        {phoneNum:<12s}           ")
        print()
        print("----------------------------------------------")
        print()
        print("                  ADD-ONS                     ")
        print()
        print("----------------------------------------------")
        print(f"Number of Cars:      {numCars:<1d}             ")
        print(f"Extra Liability:     {extraLiab:<1s}           ")
        print(f"Glass Coverage:      {glassCoverage:<1s}       ")
        print(f"Loaner Car:          {loanerCar:<1s}           ")
        print(f"payment Method:      {paymentMethod:<1s}       ")
        print()
        print("----------------------------------------------")
        print()
        print("              PAYMENT INFORMATION             ")
        print() 
        print("----------------------------------------------")
        print(f"Down Payment Amount: {FV.FDollar2(downPayment):>8s}")
        print(f"Extra Cost:          {FV.FDollar2(totalExtraCost):>8s}")
        print(f"Insurance Premium:    {FV.FDollar2(totalInsurancePremium):>8s}")
        print(f"HST:                 {FV.FDollar2(HST):>8s}")
        print(f"Total Cost:           {FV.FDollar2(finalCost):>8s}")
        print()
        print(f"Monthly Payment:     {FV.FDollar2(monthlyPayment):>8s}")
        print()
        print("----------------------------------------------")
        print()
        print("              POLICY INFORMATION              ")
        print()
        print("----------------------------------------------")
        print(f"Policy Number:       {POLICY_NUM:<8d}        ")
        print(f"Policy Date:         {FV.FDateS(curDate):<8s}")
        print()
        print("----------------------------------------------")
        print()
        print("               CLAIM INFORMATION              ")
        print()
        print("----------------------------------------------")
        print(f"Claim Number:        {claimNum:<8d}          ")
        print(f"Claim Date:          {FV.FDateS(claimDate):<8s}")
        print(f"Invoice Date:        {FV.FDateS(invoiceDate):<8s}")
        print(f"First Payment Date:  {FV.FDateS(firstPaymentDate):<8s}")
        print()
        print("----------------------------------------------")
        print()
        print("               PREVIOUS CLAIMS                ")
        print()
        print("----------------------------------------------")
        print()
        print(f"CLAIM #         CLAIM DATE       AMOUNT      ")
        print("----------------------------------------------")
        if len(prevClaimLst) == 0:
            print("No previous claims!")
        else:
            for item in prevClaimLst:
                print(f"{item[0]:<4s}            {FV.FDateS(item[1]):<8}       {FV.FDollar2(float(item[2])):<8}")

        
        
        
        


        # Any housekeeping duties at the end of the program