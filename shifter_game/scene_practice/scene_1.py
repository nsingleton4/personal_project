from shifter_game.player.player_shifter import Shifter

# Example data for creating a Shifter instance
shifter_data = {
    'name': 'Goose',
    'age': 21,
    'level': 2,
    'health': 100,
    'experience': 15
}

# Create an instance of the Shifter class
shifter = Shifter(**shifter_data)

# Call the display_sheet method to print out the character's details
shifter.display_sheet()