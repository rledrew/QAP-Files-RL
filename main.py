# A program to manage data files for the One-Stop Insurance Company
# Author: Riley LeDrew

# Section for opening, reading and defining the lines within OSICDef.dat

OSICDef = open("OSICDef.dat")

read = OSICDef.readlines()
POL_NUM = read[0]
BASIC_PREM = read[1]
ADD_DISC = read[2]
LIABILITY = read[3]
GLASS_COV = read[4]
LOANER_COV = read[5]
HST_RATE = read[6]
PROC_FEE = read[7]

# Inputs
while True:
    first_nam = input('Input Customer Name here: ')
    if first_nam.isalpha() == False:
        print('Name must contain only letters, please try again.')
    else:
        break
while True:
    last_nam = input('Input Customer Name here: ')
    if last_nam.isalpha() == False:
        print('Name must contain only letters, please try again.')
    else:
        break
while True:
    address = input('Input Customer Address here: ')
    add_val = address[0]
    if add_val.isnumeric() != True:
        print('Address must start with a number')
    else:
        break
