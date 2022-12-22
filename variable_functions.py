import random

# variables

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = list()
password = ''


# this function create a pattern for the headers in the system
def header(text):
    print(len(text)*'=-')
    print(f'{text:^{len(text)*2}}')
    print(len(text)*'=-')
    print()


# this function validate if the user type a integer
def validate_integer(item):
    while True:
        choice = input(
            f'✅ How many {item} would you like in your password?\n➡ ')
        if choice.isnumeric() and item == 'letters' and int(choice) <= len(letters) and int(choice) > 0:
            break
        if choice.isnumeric() and item == 'numbers' and int(choice) <= len(numbers) and int(choice) > 0:
            break
        if choice.isnumeric() and item == 'symbols' and int(choice) <= len(symbols) and int(choice) > 0:
            break
        else:
            print('❌ Enter with a valid number')
    return int(choice)


# this function takes the item's numbers choosen and returns this one in a randomic way
def random_items(letters_choosen, letters):
    password_list = list()
    for n in range(0, letters_choosen):
        while True:
            x = random.choice(letters)
            if x not in password_list:
                password_list.append(x)
                break
    return password_list
