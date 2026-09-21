contact_list = {}

menu_text = """
┌──────────────────────────────────────────────┐
│              --- PHONE BOOK ---              │
│    1- Add contact                            │
│    2- Add number to contact                  │
│    3- Search for a phone number by name      │
│    4- Remove contact                         │
│    5- Amount of contact                      │
│    6- Exit                                   │
└──────────────────────────────────────────────┘

"""

exit_response = """
┌────────────────────────────┐
│    Have a great time =]    │
└────────────────────────────┘"""


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


def add_contact():
    contact_name = input("• Enter the contact's name : ")

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


while True:

    user_choice = input(f"{menu_text}• Enter a number between 1 to 6 : ")

    result_message = ""

    # Exit
    if user_choice == "6":
        print(exit_response)
        break

    # 1- Add contact
    elif user_choice == "1":
        result_message = add_contact()

    # 2- Add number to contact
    elif user_choice == "2":
        pass

    # 3- Search for a phone number by name
    elif user_choice == "3":
        pass

    # 4- Remove contact
    elif user_choice == "4":
        pass

    # 5- Amount of contact
    elif user_choice == "5":
        pass

    # Invalid choice
    else:
        print("""
┌────────────────────────────┐
│    Invalid Choice (1-6)    │
└────────────────────────────┘
""")

    if continue_cycle(result_message):
        break
