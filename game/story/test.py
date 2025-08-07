from characters.player_druid import Druid

intro_dialogue = {
    "boss_office": {
        "text": "You walk into your boss' office.",
        "description": (
            "An ornate wooden office that has seen years of use. \n"
            "Creaking wooden floors accompany every step. \n"
            "He tells you, 'Get fucked kiddo you're moving out.' \n",
        ),
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
            {"text": "Go to the armourer."},
            {"text": "Go to Ayala."},
            {"text": "Go to your house."}
        ]
    },
    "boss_disappointment": {
        "text": "Talk to me like that again boy and I'll shove that dulled spear up your ass. Get going to the armorer, you don't have a choice in this.",
        "description": (
            "You walk about after the scolding, annoyed. 'Why me', you wonder. \n",
            "You appreciate the breeze that usually accompanies a storm approaching.The summer heat has been brutal this year. \n"
            "You see Calhoun's, the armourer, and your friend, Ayala. \n",
        ),
        "choice":[
            {"text": "Go to the armourer."},
            {"text": "Go to Ayala."},
            {"text": "Go to your house."}
        ]
    }
}
