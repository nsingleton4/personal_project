from characters.player_druid import Druid

def start_intro_dialogue():
    current_node = intro_dialogue["boss_office"]

    while current_node["choice"]:
        print(current_node["text"])
        print(current_node["description"])

        for i, choice in enumerate(current_node["choice"]):
            print(f"{i + 1}: {choice["text"]}")

        user_input = int(input("Choose an option: ")) - 1
        next_id = current_node["choice"][user_input]["next_node_id"]
        current_node = intro_dialogue[next_id]

intro_dialogue = {
    "boss_office": {
        "text": "\nYou were summoned to the center of the grove where only tribunal councils typically occur.\n",
        "description": "The ornate stone council bench has seen years of use. \nHe tells you, 'Get fucked kiddo you're moving out.' \n",
        "choice": [
            {"text": "Get ready.", "next_node_id": "boss_approval"},
            {"text": "Tell him off.", "next_node_id": "boss_disappointment"},
            {"text": "Open Character Sheet.", "next_node_id": "open character sheet"}
        ]
    },
    "boss_approval": {
        "text": "Go and grab your gear, make sure to swing by Calhoun's to sharpen your spear before you go.",
        "description": (
            "You walk outside and appreciate the breeze that usually accompanies a storm approaching. The summer heat has been brutal this year. \n"
            "You see Calhoun's, the armourer, and your friend, Ayala.",
        ),
        "choice": [
            {"text": "Go to the armourer.", "next_node_id": "armorer"},
            {"text": "Go to Ayala.", "next_node_id": "ayala"},
            {"text": "Go to your house.", "next_node_id": "house"}
        ]
    },
    "boss_disappointment": {
        "text": "Talk to me like that again boy and I'll shove that dulled spear up your ass. Get going to the armourer, you don't have a choice in this.",
        "description": (
            "You walk about after the scolding, annoyed. 'Why me', you wonder.\n"
            "You appreciate the breeze that usually accompanies a storm approaching. The summer heat has been brutal this year.\n"
            "You see Calhoun's, the armourer, and your friend, Ayala."
        ),
        "choice": [
            {"text": "Go to the armourer.", "next_node_id": "armorer"},
            {"text": "Go to Ayala.", "next_node_id": "ayala"},
            {"text": "Go to your house.", "next_node_id": "house"}
        ]
    },
    "armorer": {
        "text": "You enter Calhoun's shop.",
        "description": "bout time",
        "choice": [
            {"text": "Go to Ayala.", "next_node_id": "ayala"},
            {"text": "Go to your house.", "next_node_id": "house"
        ]
    },
    "ayala": {
        "text": "Ayala looks up from her book as you approach.",
        "description": "finally awake",
        "choice": [
            {"text": "Go to the armourer.", "next_node_id": "armorer"},
            {"text": "Go to your house.", "next_node_id": "house"}
        ]
    },
    "house": {
        "text": "You head home to pack your things.",
        "description": "",
        "choice": [
            {"text": "Go to the armourer.", "next_node_id": "armorer"},
        ]
    },
    "open character sheet": {
        "text": "Character Sheet:",
        "action": lambda: print(Druid.display_sheet())
    }
}

def give_xp(current_node):
    if current_node == "armorer":
        Druid.experience.set(Druid.experience.get() + 5)
    else:
        return