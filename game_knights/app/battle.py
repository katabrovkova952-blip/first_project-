from game_knights.app import Knight


def fight(player_1: Knight, player_2: Knight) -> dict:
    power_1 = player_1.total_power()
    hp_1 = player_1.total_hp()
    protection_1 = player_1.total_protection()

    power_2 = player_2.total_power()
    hp_2 = player_2.total_hp()
    protection_2 = player_2.total_protection()

    hp_1 -= power_2 - protection_1
    hp_2 -= power_1 - protection_2
    if hp_1 <= 0:
        hp_1 = 0

    if hp_2 <= 0:
        hp_2 = 0
    return {player_1.name : hp_1, player_2.name : hp_2}


def make_knight(data):
    return Knight(
        data["name"],
        data["power"],
        data["hp"],
        data["armour"],
        data["weapon"],
        data["potion"],
    )


def battle(knights_config):
    lancelot = make_knight(knights_config["lancelot"])
    arthur = make_knight(knights_config["arthur"])
    mordred = make_knight(knights_config["mordred"])
    red_knight = make_knight(knights_config["red_knight"])

    result = {}

    result.update(fight(lancelot, mordred))
    result.update(fight(arthur, red_knight))

    return result


