# Main menu displayed to the user
menu_text = """
┌──────────────────────────────────────────────┐
│              --- PHONE BOOK ---              │
│    1- Add contact                            │
│    2- Add number to contact                  │
│    3- Search for a phone number by name      │
│    4- Remove contact                         │
│    5- Amount of contact                      │
│    6- Show all contacts                      │
│    7- Exit                                   │
└──────────────────────────────────────────────┘

"""

# Message displayed when the program exits
EXIT_RESPONSE = """
┌────────────────────────────┐
│    Have a great time =]    │
└────────────────────────────┘
"""

# Error message for invalid phone numbers
PHONE_NUMBER_ERROR = """
┌───────────────────────────────────────────────┐
│    The phone number must be 11 digits long    │
└───────────────────────────────────────────────┘
"""

# Message displayed when a contact already exists
CONTACT_EXISTS_MESSAGE = """
┌───────────────────────────────────────────────┐
│    A contact with this name already exists    │
└───────────────────────────────────────────────┘
"""

# Message displayed after successfully adding a contact
CONTACT_ADDED_MESSAGE = """
┌──────────────────────────────────┐
│    Contact successfully added    │
└──────────────────────────────────┘
"""

# Message displayed when a contact cannot be found
CONTACT_NOT_FOUND_MESSAGE = """
┌───────────────────────────────────────┐
│    No contact found with this name    │
└───────────────────────────────────────┘
"""

# Message displayed after successfully adding a new number
NUMBER_ADDED_MESSAGE = """
┌─────────────────────────────────────────┐
│    The new number successfully added    │
└─────────────────────────────────────────┘
"""

# Message displayed after successfully removing a contact
CONTACT_REMOVED_MESSAGE = """
┌────────────────────────────────────────┐
│    The contact successfully removed    │
└────────────────────────────────────────┘
"""

# Message displayed when there are no contacts
CONTACT_LIST_EMPTY_MESSAGE = """
┌─────────────────────────────┐
│    Contact list is empty    │
└─────────────────────────────┘
"""

# Message displayed when the user enters an invalid menu choice
INVALID_CHOICE_MESSAGE = """
┌────────────────────────────┐
│    Invalid Choice (1-7)    │
└────────────────────────────┘
"""


# Get and validate a phone number
def get_phone_number():
    while True:
        phone_number = input("• Enter the phone number : ")

        if len(phone_number) == 11 and phone_number.isdigit():
            return phone_number

        print(PHONE_NUMBER_ERROR)


# Get contact name
def get_contact_name():
    return input("• Enter the contact's name : ").strip()


# Add a new contact to the phone book
def add_contact(contact_list):
    contact_name = get_contact_name()

    if contact_name in contact_list:
        return CONTACT_EXISTS_MESSAGE

    phone_number = get_phone_number()
    contact_list[contact_name] = [phone_number]

    return CONTACT_ADDED_MESSAGE


# Add another phone number to an existing contact
def add_number_to_contact(contact_list):
    contact_name = get_contact_name()

    if contact_name not in contact_list:
        return CONTACT_NOT_FOUND_MESSAGE

    new_phone_number = get_phone_number()
    contact_list[contact_name].append(new_phone_number)

    return NUMBER_ADDED_MESSAGE


# Search for a contact and display its phone numbers
def search_contact(contact_list):
    contact_name = get_contact_name()

    if contact_name not in contact_list:
        return CONTACT_NOT_FOUND_MESSAGE

    phone_numbers = contact_list[contact_name]
    phone_numbers_text = "\n  ".join(phone_numbers)

    return f"""
- {contact_name} :
  {phone_numbers_text}
"""


# Remove a contact from the phone book
def remove_contact(contact_list):
    contact_name = get_contact_name()

    if contact_name not in contact_list:
        return CONTACT_NOT_FOUND_MESSAGE

    del contact_list[contact_name]

    return CONTACT_REMOVED_MESSAGE


# Display all contacts and their phone numbers
def show_all_contacts(contact_list):
    if not contact_list:
        return CONTACT_LIST_EMPTY_MESSAGE

    contact_text = ""

    for contact_name, phone_numbers in contact_list.items():
        contact_text += f"\n- {contact_name}\n"

        for phone_number in phone_numbers:
            contact_text += f"    {phone_number}\n"

    return contact_text


# Ask the user whether they want to continue or exit
def continue_cycle(result_message):
    continue_prompt = """
• Do you want to continue? (Yes/No)
- """

    continue_choice = input(result_message + continue_prompt).lower()
    remaining_attempts = 3

    while remaining_attempts > 0:

        if continue_choice == "yes":
            return False

        if continue_choice == "no":
            print(EXIT_RESPONSE)
            return True

        remaining_attempts -= 1

        print("""
┌──────────────────────────────┐
│    Invalid Input (Yes/No)    │
└──────────────────────────────┘
""")

        if remaining_attempts == 0:
            print("""
┌──────────────────────────────────┐
│    Too many invalid attempts!    │
│          Program closed.         │
└──────────────────────────────────┘
""")
            return True

        print(f"You have {remaining_attempts} attempts left")
        continue_choice = input(continue_prompt).lower()


# Main program loop
def main():
    contact_list = {}

    while True:
        user_choice = input(
            f"{menu_text}• Enter a number between 1 to 7 : "
        )

        # Exit the program
        if user_choice == "7":
            print(EXIT_RESPONSE)
            break

        # Add a new contact
        elif user_choice == "1":
            result_message = add_contact(contact_list)

        # Add another number to an existing contact
        elif user_choice == "2":
            result_message = add_number_to_contact(contact_list)

        # Search for a contact by name
        elif user_choice == "3":
            result_message = search_contact(contact_list)

        # Remove a contact
        elif user_choice == "4":
            result_message = remove_contact(contact_list)

        # Show the total number of contacts
        elif user_choice == "5":
            result_message = f"Quantity of Contacts >>> {len(contact_list)} \n"

        # Show all contacts
        elif user_choice == "6":
            result_message = show_all_contacts(contact_list)

        # Handle invalid menu choices
        else:
            result_message = INVALID_CHOICE_MESSAGE

        # Ask for continue
        if continue_cycle(result_message):
            break


main()
