# A program to manage data files for the One-Stop Insurance Company
# Author: Riley LeDrew

# Section for opening, reading and defining the lines within OSICDef.dat

OSICDef = open("OSICDef.dat")  # Opening file
read = OSICDef.readlines()  # Assigning variable to the read function
POL_NUM = int(read[0])  # Policy number from defaults file
BASIC_PREM = float(read[1])  # Basic premium cost from defaults file
ADD_DISC = float(read[2])  # Discount for each additional car as a percent, from defaults file
LIABILITYFEE = float(read[3])  # Fee for liability insurance for each car from defaults file
GLASS_COVFEE = float(read[4])  # Fee for glass coverage for each car from defaults file
LOANER_COVFEE = float(read[5])  # Fee for insurance on loaner cars from defaults file
HST_RATE = float(read[6])  # Rate of sales tax from defaults file
PROC_FEE = float(read[7])  # Processing fee for 8 monthly payments from defaults file
# Inputs
while True:
    first_nam = input('Input Customer Name here: ').title()
    if first_nam.isalpha() is False:
        print('Name must contain only letters, please try again.')
    else:
        break
while True:
    last_nam = input('Input Customer Name here: ').title()
    if last_nam.isalpha() is False:
        print('Name must contain only letters, please try again.')
    else:
        break
while True:
    address = input('Input Customer Street Address here: ').title()
    add_val = address[0]
    if add_val.isnumeric() is False:
        print('Address must start with a number')
    else:
        break
while True:
    city = input('Input Customer City here: ').title()
    cityval = city.replace(' ', '')  # Cityval is only used for validation, city should be used normally.
    if cityval.isalpha() is False:
        print('Customer City must contain only letters')
    else:
        break
while True:
    province = input('Input Customer Province here (Format XX): ').upper()
    if len(province) != 2:
        print('Length of Province abbreviation must be 2')
    elif province.isalpha() is False:
        print('Province abbreviation must contain only letters')
    else:
        break
while True:
    postal = input('Input Customer postal code here (X#X #X#): ').upper()
    postal = postal.replace(' ', '')
    if postal[0].isalpha() is False or postal[2].isalpha() is False or postal[4].isalpha() is False:
        print('Postal code must be in format X#X #X#')
    elif postal[1].isdigit() is False or postal[3].isdigit() is False or postal[5].isdigit() is False:
        print('Postal code must be in format X#X #X#')
    elif len(postal) != 6:
        print('Postal code must be 6 characters long')
    else:
        break

while True:
    phone = input('Input Customer Phone Number here (Format ###-###-####): ')
    phone = phone.replace(' ', '')
    phone = phone.replace('-', '')
    if len(phone) != 10:
        print('Length of Phone Number must be 10')
    elif phone.isdigit() is False:
        print('Phone Number must contain only numbers')
    else:
        break
while True:
    car = input('Input number of Cars being insured here: ')
    carflt = float(car)  # Had to redefine car as float, within the loop as to not leave it undefined.
    if car.isdigit() is False:
        print('Number of cars must contain only digits')
    elif carflt <= 0:
        print('Number of cars cannot be 0 or less')
    else:
        break
while True:
    liability = input('Would you like to add Liability Insurance up to $1,000,000?(Y/N): ').upper()
    if liability == 'Y':
        break
    elif liability == 'N':
        break
    else:
        print('Please choose a valid input')
while True:
    glass = input('Would you like to add Glass Coverage?(Y/N): ').upper()
    if glass == 'Y':
        break
    elif glass == 'N':
        break
    else:
        print('Please choose a valid input')
while True:
    loaner = input('Would you like to add Loaner Coverage?(Y/N): ').upper()
    if loaner == 'Y':
        break
    elif loaner == 'N':
        break
    else:
        print('Please choose a valid input')
while True:
    paymentopt = input('Would you like to pay in Full or Monthly?(F/M): ').upper()
    if paymentopt == 'F':
        break
    elif paymentopt == 'M':
        break
    else:
        print('Please choose a valid input')

# Processing Section

premiums = BASIC_PREM + ((carflt - 1) * (BASIC_PREM * (1.00 - ADD_DISC)))
addfees = 0
if liability == 'Y':
    addfees += (LIABILITYFEE * carflt)
else:
    pass
if glass == 'Y':
    addfees += (GLASS_COVFEE * carflt)
else:
    pass
if loaner == 'Y':
    addfees += (LOANER_COVFEE * carflt)
else:
    pass
subtotal = addfees + premiums
hst = subtotal * HST_RATE
total = subtotal + hst
monthly = (total + PROC_FEE) / 8
# Hey future Riley, it's past Riley. Make sure you don't forget to format phone number and postal code properly after removing spaces / dashes
# You can do this by taking the index of a section, for example the first 3 digits in the phone num, and concatenate them with a -, then the next 3 digits and so on.