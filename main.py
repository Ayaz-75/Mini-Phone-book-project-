contacts = {}

def add_contact():
    # Input name, phone number, and optionally email
    global contacts
    name_input = input("Enter name of the contact: ")
    phone_input = input("Enter the phone number along with country code: ")
    email_input = input("Enter the email of the contact: ")
    contacts[name_input] = {
        phone_input,
        email_input
    }


def view_contact():
    global contacts
    if not contacts:
        print("There is no contact inside the Phonebook yet!")
    else:
        for i in contacts:
            print(f"{i}: {contacts[i]}")


def search_contact():
    global contacts
    contact_search = input("Enter the name of the contact: ")

    if len(contacts) == 0:
        print(f"There is no contact inside the Phonebook yet!")
    # Search by name and return their info
    elif contact_search in contacts:
        print(contacts[contact_search])
    else:
        print(f"You want to search {contact_search} which is not in Phonebook yet!")
    

def delete_contact():
    # Delete a contact by name
    global contacts
    contact_to_delete = input("Enter the contact to delete: ")
    if len(contacts) == 0:
        print(f"There is no contact inside the Phonebook yet!")
    elif contact_to_delete in contacts:
        del contacts[contact_to_delete]
    else:
        print(f"You want to delete {contact_to_delete} which is not in Phonebook yet!")
def exit():
    # Exit the program gracefully
    print("goodbye!")


print("----------------------------------------")
print()
print("Welcome to the digital phonebook")

should_stop_asking = False
while not should_stop_asking:

    your_choice = int(input(f"What do you want to do\n1-Add contact\n2-View contact\n3-Search contact\n4-Delete contact\n5- exit: "))
    if your_choice == 1:
        add_contact()
    elif your_choice == 2:
        view_contact()
    elif your_choice == 3:
        search_contact()
    elif your_choice == 4:
        delete_contact()
    elif your_choice == 5:
        exit()
        should_stop_asking = True
