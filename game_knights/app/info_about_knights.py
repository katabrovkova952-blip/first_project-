from game_knights.app import Knight
lancelot = Knight("Lancelot",35,100,[],{"name": "Metal Sword", "power": 50,},None)

arthur = Knight("Arthur",45,75,[{'part': 'helmet', 'protection': 15},
                                                         {'part': 'breastplate', 'protection': 20},
                                                         {'part': 'boots', 'protection': 10}],
                                                  {"name": "Two-handed Sword", "power": 55,},None)

mordred = Knight("Mordred",30,90,[{'part': 'breastplate', 'protection': 15},
                                                         {'part': 'boots', 'protection': 10}],
                                                  {"name": "Poisoned Sword", "power": 60,}, {
                                                          "name": "Berserk",
                                                          "effect": { "power": +15, "hp": -5,
                                                          "protection": +10}})

red_knight = Knight("Red Knight",40,70,[{'part': 'breastplate', 'protection': 25}],
                                                  {"name": "Sword", "power": 45,}, {
                                                          "name": "Blessing",
                                                          "effect": { "power": +5, "hp": +10,}})