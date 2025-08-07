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
        "text": "\nYou walk into your boss' office.\n",
        "description": "An ornate wooden office that has seen years of use. \nCreaking wooden floors accompany every step. \nHe tells you, 'Get fucked kiddo you're moving out.' \n",
        "choice": [
            {"text": "Get ready.", "next_node_id": "boss_approval"},
            {"text": "Tell him off.", "next_node_id": "boss_disappointment"}
        ]
    },
    "boss_approval": {
        "text": "Go and grab your gear, make sure to swing by Calhoun's to sharpen your spear before you go.",
        "description": (
            "You walk outside and appreciate the breeze that usually accompanies a storm approaching. The summer heat has been brutal this year. \n"
            "You see Calhoun's, the armourer, and your friend, Ayala.",
        ),
        "choice": [
            {"text": "Go to the armourer.", "next_node_id": "armourer"},
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
            {"text": "Go to the armourer.", "next_node_id": "armourer"},
            {"text": "Go to Ayala.", "next_node_id": "ayala"},
            {"text": "Go to your house.", "next_node_id": "house"}
        ]
    },
    "armourer": {
        "text": "You enter Calhoun's shop.",
        "description": "Calhoun grunts as he sees you. 'Bout time you came in.'",
        "choice": []  # End or continue
    },
    "ayala": {
        "text": "Ayala looks up from her book as you approach.",
        "description": "'Hey, you're finally heading out?' she asks.",
        "choice": []
    },
    "house": {
        "text": "You head home to pack your things.",
        "description": "The house is quiet. You feel the weight of the journey ahead.",
        "choice": []
    }
}
