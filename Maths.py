

# from Calculator import Calculator

# print("Select operation.")
# print("1.Basic Calculator")     
# print("2.Area")
# print("3.Multiply")
# print("4.Divide")
# print("5.BACK")

# while True:
#     choice = int(input("Enter Choice:1/2/3/4/5:"))
#     if choice == 1:
#         while True:
#             Calculator()
#     elif choice == 2:
#         Calculator()
#     elif choice == 5:
#         exit()
# Menu-Driven program

import string
import random

from Calculator import Calculator
from area import Area
from perimeter import Perimeter
from sort_edited import Sort
from cc_updated import converter
from LCM_GCD import lcmgcd
from hype import hypotenuse
from day_validator_update import day_calculator
from timeconverter import tc



while True:
    
    from datetime import datetime
    str=datetime.now()
    now=str.strftime("%d/%m/%y %H:%M:%S")
    print(now)

    print('\nChoose your Option - ')
    print('0. Exit')
    print('1. Basic Calculator')
    print('2. Area calculator')
    print('3. Perimeter calculator')
    print('4. List Sorting')
    print('5. LCM & GCD')
    print('6. Day Calculator')
    print('7. Hypotenuse Calculator')
    print('8. Seconds Converter')
    print('9. Currency Converter')
    option = input('Enter - ')
    try:
        option = int(option)
    except:
        print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
        continue
    
    if (option < 0 or option > 9):
        print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
        continue
    
    if option == 0:
        print('\n\tTHANK YOU FOR JOINING US!')
        exit(-1)
    elif option == 1:
        Calculator()
    elif option == 2:
        Area()
    elif option == 3:
        Perimeter()
    elif option == 4:
        Sort()
    elif option == 5:
        lcmgcd()
    elif option == 6:
        day_calculator()
    elif option == 7:
        hypotenuse()
    elif option == 8:
        tc()
    elif option == 9:
        converter()                
