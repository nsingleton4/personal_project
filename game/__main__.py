from characters.player_druid import Druid
from story.test import game_test

def character_input():
    # making the initial input "False"
    correct_input = False
    # character name is blank initially
    new_char = None
    # this is where the inputs override the false tags above
    while not correct_input:
        input_name = input("\nWhat is your name?  >>>  ")
        input_class = input("\nWhat kind of character do you want?  >>>   ")
        # if this class is druid, then it will return new_char
        if input_class.lower() == "druid":
            new_char = Druid(name=input_name)
            # this is what overrides the initial false tag based on the inputs
            correct_input = True
        else:
            print(f"\n{input_class} is not a valid character type")
            # returns the function that is defined as new char
    return new_char

# creates an object of character using the function
char1 = character_input()

# uses the object using character_input and the display sheet function of Druid to make the character sheet
char1.display_sheet()

my_input_3 = input("\nBegin adventure? (yes or no) >>>  ")

if my_input_3.lower() == "yes":
    game_test()
else:
    print(f"Your adventure ends. Come back when you're ready.")
