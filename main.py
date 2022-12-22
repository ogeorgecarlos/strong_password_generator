'''
This system will generate a strong password for the user
this password will have how many  letters, numbers and special symbols...
as the user wants.
Behind the user to choice the number of characters for each type
the program will choice and returns in a randomic way,..
with no repeated characters and scrambled between each other
'''
from variable_functions import (letters, numbers, password, password_list,
                                random_items, symbols, validate_integer, header)
import random

# -- MAIN PROGRAM --

header("🔗 Welcome to the PyPassword Generator!")

# here the user will input how how many character of each item he/she want
letters_choosen = validate_integer('letters')
symbols_choosen = validate_integer('symbols')
numbers_choosen = validate_integer('numbers')

# Here each character of the password will be appended in a list in a randomic way
password_list.extend(random_items(letters_choosen, letters))
password_list.extend(random_items(numbers_choosen, numbers))
password_list.extend(random_items(symbols_choosen, symbols))

# After the list append all characters , this will be shuffled
random.shuffle(password_list)

# and pritend like a string of random characters
for letra in password_list:
    password += letra

# finish :)
header("✅ Your Password is finished!")
print(f'\033[31m{password:^40}\033[m')
