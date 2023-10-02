''' WAP to calculate your tax input
    a. income<10000, tax=0%
    b. income>10000 and income<50000, tax=5%
    c. income>50000 and income<100000, tax=10%
    d. income>100000, tax=15%
'''

def taxcalculation(income):

    if income<10000:
        tax=0
        return tax
    elif income>10000 and income<50000:
        tax=(5*income)/100
        return tax
    elif income>50000 and income<100000:
        tax=(10*income)/100
        return tax
    else:
        tax=(income*15)/100
        return tax

income=int(input("Enter your amount"))
print('Your tax amount is',taxcalculation(income))
