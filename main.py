from operation import*
from termcolor import colored
print(colored("  Contact Project  ".center(50, '*'), color="yellow"))

def start():
    print(colored(
    """
    Option List:

    1.Display Contacts from the Database.
    2.Add New Contact to the Database.
    3.Update Contact.
    4.Delete Contact from the Database by ID.
    5.Stop the Program.
    """, color="blue"))

    # get option from the user
    user_choice = input("Enter your choice:  ").strip()

    if user_choice.isnumeric() and 0 < int(user_choice) < 6:
        option = int(user_choice)

        if option == 1:
            showAllData()
            back()
        if option == 2:
            addNewData()
            back()
        if option == 3:
            updateDataFromId()
            back()
        if option == 4:
            delcontactbyId()
            back()
        if option == 5:
            back(True)
    else:
        print("You can only choose from 1-5!")
        start()

def back(is_exit = False):
    if is_exit == False:
        if input("Back to Option List ? (Y)").lower() == 'y':
            start()
        
    print(colored("The program was terminated successfully.", color="green"))


# first call
start()



