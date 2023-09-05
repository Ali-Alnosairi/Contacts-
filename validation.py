import re
import colored


def isValidName(name):
    if name == "":
        print(colored("Name is required !", color="red"))
        return False

    if not name.isalpha():
        print(colored("Name must be only alphabets !", color="red"))
        return False
    return True


def isValidEmail(email):
    if email == "":
        print(colored("E-mail is required !", color="red"))
        return False

    # {2,} at least two characters after dot .
    pattern = r"^[a-zA-Z0-9\._%+!#$&~-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}$"

    # check if the pattern matches the email address
    match = re.match(pattern, email)

    if not match:
        print(colored("Invalid E-mail!", color="red"))
        return False

    return True


def isValidPhone(phone):
    if phone == "":
        print(colored("Phone is required !", color="red"))
        return False

    if not phone.isnumeric():
        print(colored("Phone should be only numbers !", color="red"))
        return False

    # pattern for Yemeni cell phone number
    cell_phone_pattern = r"^((\+|00)9677|7)[01378]\d{7}$"

    # compare the input number with cell phone number pattern
    matchcell_phone_pattern = re.match(cell_phone_pattern, str(phone))

    # pattern for Yemeni home number
    home_pattern = r"^((\+|00)967|0)[1-7]\d{6}$"

    # compare the input number with home number pattern
    match_home_pattern = re.match(home_pattern, str(phone))

    # check if the input number is an Yemeni cell phone number OR home number
    if not matchcell_phone_pattern and not match_home_pattern:
        print(colored("Invalid Phone number!", color="red"))
        return False

    return True
