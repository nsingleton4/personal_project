from shifter_game.dice import roll_dice

# use dictionary rather than class for character

player = {
    "inventory": {
        "weapons": {
            "staff": None
        },
        "clothes": {
            "shirt": None
        },
        "pouch": {
            "herbs": None
        }
    },
    "name": None,
    "statistics": {
        "strength": None,
        "dexterity": None,
        "wisdom": None
        # make a dice function to apply random numbers to stats
        }

}


p1 = player.copy()

name = input("What is your name\n Enter name >>> ")
p1["name"] = name
print(f'Hello {p1["name"]}')

print(p1["statistics"]["wisdom"])
print(p1["name"])

print(roll_dice(d20 = True))


# def character_input():
#     # making the initial input "False"
#     correct_input = False
#     # character name is blank initially
#     new_char = None
#     # this is where the inputs override the false tags above
#     while not correct_input:
#         input_name = input("\nWhat is your name?  >>>  ")
#         input_class = input("\nYou will either shift the world around you or be shifted by it (type ready to start)  >>>   ")
#         # if this class is druid, then it will return new_char
#         if input_class.lower() == "ready":
#             new_char = Shifter(name=input_name)
#             # this is what overrides the initial false tag based on the inputs
#             correct_input = True
#     return new_char
#
# # creates an object of character using the function
# char1 = character_input()
#
# # uses the object using character_input and the display sheet function of Druid to make the character sheet
# char1.display_sheet()
#
# # my_input_3 = input("\nBegin adventure? (yes or no) >>>  ")
# #
# # while True:
# #     if my_input_3.lower() == "yes":
# #         start_intro_dialogue()
# #     elif my_input_3.lower() not in {'quit', 'no'}:
# #         break
# #     else:
# #         my_input_3 = input("\n \"{}\" is not a valid entry. Begin adventure? (yes or no) >>>  ".format(my_input_3))
# # print(f"Your adventure ends. Come back when you're ready.")
