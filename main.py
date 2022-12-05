# A program to manage data files for the One-Stop Insurance Company
# Author: Riley LeDrew

while True:
    # Section for opening, reading and defining the lines within OSICDef.dat
    POLICIES = open('Policies.dat', 'a')
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
    city = input('Input Customer City here: ').title()
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
        postal = postal.replace('-', '')
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

    # Display Section for receipt
    postaldsp = f'{postal[0]}{postal[1]}{postal[2]} {postal[3]}{postal[4]}{postal[5]}'
    policydsp = f'{POL_NUM}'
    phonedsp = f'{phone[0]}{phone[1]}{phone[2]}-{phone[3]}{phone[4]}{phone[5]}-{phone[6]}{phone[7]}{phone[8]}{phone[9]}'
    totaldsp = f'${total:.2f}'
    hstdsp = f'${hst:.2f}'
    subtotaldsp = f'${subtotal:.2f}'
    monthlydsp = f'${monthly:.2f}'
    headerdsp = 'One Stop Insurance Company Policy Receipt'
    fullnamedsp = f'{first_nam} {last_nam}'
    liabilitydsp = 'Maybe'
    glassdsp = 'Maybe'
    loanerdsp = 'Maybe'
    paymentoptdsp = 'Maybe'

    if liability == 'Y':
        liabilitydsp = 'Yes'
    else:
        liabilitydsp = 'No'
    if glass == 'Y':
        glassdsp = 'Yes'
    else:
        glassdsp = 'No'
    if loaner == 'Y':
        loanerdsp = 'Yes'
    else:
        loanerdsp = 'No'
    if paymentopt == 'F':
        paymentoptdsp = 'Full'
    else:
        paymentoptdsp = 'Monthly'

    # Print Section

    print('=' * 64)
    print(f'{headerdsp:^64}')
    print('')
    print(f'Policy Number: {policydsp:>49}')
    print(f'Customer Name: {fullnamedsp:>49}')
    print(f'Customer Street: {address:>47}')
    print(f'Customer City: {address:>49}')
    print(f'Customer Province: {address:>45}')
    print(f'Customer Postal Code: {postaldsp:>42}')
    print(f'Customer Phone Number: {phonedsp:>41}')
    print(f'Number of cars to be insured: {car:>34}')
    print(f'Add Liability insurance up to $1,000,000?: {liabilitydsp:>22}')
    print(f'Add glass coverage? {glassdsp:>44}')
    print(f'Add loaner coverage? {loanerdsp:>43}')
    print(f'Pay in full or 8 month plan? {paymentoptdsp:>35}')
    print('')
    print('')
    print('')
    print(f'Subtotal: {subtotaldsp:>54}')
    print(f'HST: {hstdsp:>59}')
    print(f'Total: {totaldsp:>57}')
    if paymentopt == 'M':
        print(f'Monthly payment due: {monthlydsp:>43}')
    print('=' * 64)
    Selection = input("Press any key to continue... ")

    # File operations

    POLICIES.write(f'{policydsp},{first_nam},{last_nam},{address},{city},{province},{postal},{phonedsp},{car}\
,{liability},{glass},{loaner},{paymentopt},{total:.2f}')
    OSICDef.close()
    POL_NUM += 1
    def replace_line(file_name, line_num, text):
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()
    replace_line('OSICDef.dat', 0, f'{POL_NUM}\n')
    # Whitespace
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    choice = input('Would you like to run the program again? (Y/N): ').upper()
    if choice == 'N':
        break
    else:
        pass
