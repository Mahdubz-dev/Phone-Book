contact_list = {}

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

exit_response = """
┌────────────────────────────┐
│    Have a great time =]    │
└────────────────────────────┘"""


# Get and validate a phone number
def get_phone_number():

    while True:

        phone_number = input("• Enter the phone number : ")

        if len(phone_number) == 11 and phone_number.isdigit():
            return phone_number

        print("""
┌───────────────────────────────────────────────┐
│    The phone number must be 11 digits long    │
└───────────────────────────────────────────────┘
""")


# Get contact name
def get_contact_name():
    return input("• Enter the contact's name : ").strip()


# Add a new contact to the phone book
def add_contact():
    contact_name = get_contact_name()

    if contact_name in contact_list:

        return """
┌───────────────────────────────────────────────┐
│    A contact with this name already exists    │
└───────────────────────────────────────────────┘
"""
    phone_number = get_phone_number()
    contact_list[contact_name] = [phone_number]

    return """
┌──────────────────────────────────┐
│    Contact successfully added    │
└──────────────────────────────────┘
"""


# Add an additional phone number to an existing contact
def add_number_to_contact():
    contact_name = get_contact_name()

    if contact_name not in contact_list:
        return """
┌───────────────────────────────────────┐
│    No contact found with this name    │
└───────────────────────────────────────┘
"""
    new_phone_number = get_phone_number()
    contact_list[contact_name].append(new_phone_number)

    return """
┌─────────────────────────────────────────┐
│    The new number successfully added    │
└─────────────────────────────────────────┘
"""


# Search for a contact and display its phone numbers
def search_contact():
    contact_name = get_contact_name()

    if contact_name in contact_list:
        phone_numbers = contact_list[contact_name]

        phone_numbers_text = "\n".join(phone_numbers)
        return f"""
- {contact_name} :
  {phone_numbers_text}
"""

    return """
┌───────────────────────────────────────┐
│    No contact found with this name    │
└───────────────────────────────────────┘
"""


# Remove a contact from the phone book
def remove_contact():
    contact_name = get_contact_name()

    if contact_name in contact_list:

        del contact_list[contact_name]
        return """
┌────────────────────────────────────────┐
│    The contact successfully removed    │
└────────────────────────────────────────┘
"""

    return """
┌───────────────────────────────────────┐
│    No contact found with this name    │
└───────────────────────────────────────┘
"""


# Ask for continue or exit
def continue_cycle(result_message):
    continue_prompt = """
• Do you want to continue? (Yes/No)
- """
    continue_choice = input(result_message + continue_prompt).lower()
    remaining_attempts = 3

    while remaining_attempts > 0:

        if continue_choice == "yes":
            return False

        elif continue_choice == "no":
            print(exit_response)
            return True

        else:
            remaining_attempts -= 1

            print("""
┌──────────────────────────────┐
│    Invalid Input (Yes/No)    │
└──────────────────────────────┘""")

            if remaining_attempts == 0:
                print("""
┌──────────────────────────────────┐
│    Too many invalid attempts!    │
│          Program closed.         │
└──────────────────────────────────┘""")
                return True
            print(f"You have just {remaining_attempts} attempts left")
            continue_choice = input(continue_prompt).lower()


# Display all contacts with their phone numbers
def show_all_contacts():

    if not contact_list:
        return """
┌─────────────────────────────┐
│    Contact list is empty    │
└─────────────────────────────┘
"""

    contact_text = ""

    for contact_name, phone_numbers in contact_list.items():
        contact_text += f"\n- {contact_name}\n"

        for phone_number in phone_numbers:
            contact_text += f"    {phone_number}\n"

    return contact_text


# Main program loop
while True:

    user_choice = input(f"{menu_text}• Enter a number between 1 to 7 : ")

    result_message = ""

    # Exit the program
    if user_choice == "7":
        print(exit_response)
        break

    # 1- Add a new contact
    elif user_choice == "1":
        result_message = add_contact()

    # 2- Add another phone number to an existing contact
    elif user_choice == "2":
        result_message = add_number_to_contact()

    # 3- Search for a contact by name
    elif user_choice == "3":
        result_message = search_contact()

    # 4- Remove a contact
    elif user_choice == "4":
        result_message = remove_contact()

    # 5- Show the total number of contacts
    elif user_choice == "5":
        result_message = f"Quantity of Contacts >>> {len(contact_list)}"

    # 6- Show all contacts
    elif user_choice == "6":
        result_message = show_all_contacts()

        # Handle invalid menu choices
    else:
        print("""
┌────────────────────────────┐
│    Invalid Choice (1-7)    │
└────────────────────────────┘
""")

    # Ask the user whether to continue after each operation
    if continue_cycle(result_message):
        break
