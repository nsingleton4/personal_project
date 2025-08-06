from characters.player_druid import Druid

def game_test():
    print(f"\nYou walk into your bosses office. An ornate wooden office that has seen years of use. \nCreaking wooden floors accompany every step. \nHe tells you 'Get fucked kiddo you're moving out'.")
    story_input = input(f"\nWhat do you plan to do?  >>>  ")

    if story_input.lower() == "":
        print("\nHello How are you.")
    else:
        print("\nyou have shirked your duties, your journey ends")
        return None

