from  validation import *
from json import *
from termcolor import colored



def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as file_obj:
       
        return load(file_obj)


data = getDataFormJsonFile("db.json")


def addNewData():
    # get the last id and increase it for the new ID
    id = data["contacts"][-1]["id"] + 1
    validName = False
    validEmail = False
    validPhone = False

    while not validName:
        name = input("Enter Name: ")
        validName = isValidName(name)

    while not validPhone:
        phone = input("Enter Phone Number: ")
        validPhone = isValidPhone(phone)

    while not validEmail:
        email = "".join(input("Enter Email: ").split())
        validEmail = isValidEmail(email)

    contact = {"id": id, "name": name, "phone": phone, "email": email}

    # after get the JSON data add the new contact to them and reright the all file
    # with the updated data
    data["contacts"].append(contact)
    with open("db.json", "w") as file_obj:
        # dump function write in JSON file
        dump(data, file_obj)

        print(colored("Contact added successfully", color="green"))





def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as file_obj:

        # load function read the JSON file content
        return load(file_obj)

data = getDataFormJsonFile("db.json")

def delcontactbyId():
    
    # recive id of the deleted contact from user
    _id = int(input("Enter ID: "))

    # bool var to check if the operation success or not
    find = False
    
    # search for the specific contact by its ID
    for contact in data['contacts']:
        if contact['id'] == _id:

            # pop the contact by its id index from the list
            data['contacts'].pop(data['contacts'].index(contact))
            find = True

            # print alert msg after operation success 
            print(colored(f"{_id} -The ID number has been deleted from the database", color="green"))
            break

    with open("db.json", "w") as file_obj:
        
        # dump function write in JSON file
        dump(data, file_obj)

    # check if the operation failed to print alert msg
    if find == False:
        print(colored(f"{_id} -Number ID not found", color="red"))



def getDataFormJsonFile(_fileName):

    # with replaces a try-catch block with a concise shorthand
    # using the with statement, the file closes automatically after you’ve processed the file.
    with open(_fileName, "r") as file_obj:

        # load function read the JSON file content
        return load(file_obj)

data = getDataFormJsonFile("db.json")

def showAllData():

    # print formated and colored table
    print(colored("ID:".center(5, " ")      + "|" + 
        "Name:".center(10, " ")           + "|" + 
        "Phone:".center(11, " ")          + "|" + 
        "E-mail:".center(15, " ")
        , color="blue") )
        
    print(colored("-", color="blue") * 41)

    for d in data['contacts']:
        print(f"{d['id']}".center(5, " ")     + "|" + 
            f"{d['name']}".center(10, " ")  + "|" + 
            f"{d['phone']}".center(11, " ") + "|" + 
            f"{d['email']}".center(15, " ") )



def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as file_obj:
        # load function read the JSON file content
        return load(file_obj)


data = getDataFormJsonFile("db.json")


def updateDataFromId():
    # bool var to check if the operation success or not
    found = False
    # while found != True:

    # recive id of the deleted contact from user
    _id = int(input("Enter ID: "))

    for contact in data["contacts"]:
        # check if there is a contact with this ID
        if contact["id"] == _id:
            found = True
            break

    else:
        print(colored("There is no contact with this ID", color="red"))

    if found == False:
        print(colored("No change was happened!", color="red"))

    else:
        validName = False
        validEmail = False
        validPhone = False

        while not validName:
            name = input("Enter Name: ")
            validName = isValidName(name)

        while not validPhone:
            phone = input("Enter Phone Number: ")
            validPhone = isValidPhone(phone)

        while not validEmail:
            email = "".join(input("Enter Email: ").split())
            validEmail = isValidEmail(email)

        # change contact data
        contact["name"] = name
        contact["phone"] = phone
        contact["email"] = email

        with open("db.json", "w") as file_obj:
            # dump function write in JSON file
            dump(data, file_obj)

            # TODO: color green
            print(
                colored(
                    f"Data of contact with ID {_id} updated successfully!",
                    color="green",
                )
            )




