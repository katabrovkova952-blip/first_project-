class Knight:
    def __init__(self, name, power, hp, armours=None, weapon=None, potion=None):
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours or []
        self.weapon = weapon or {}
        self.potion = potion or {}

    def total_power(self):
        power = self.power
        power += self.weapon.get("power", 0)
        if self.potion:
            power += self.potion["effect"].get("power", 0)
        return power

    def total_hp(self):
        hp = self.hp
        if self.potion:
            hp += self.potion["effect"].get("hp", 0)
        return hp

    def total_protection(self):
        protection = sum(armour["protection"] for armour in self.armours)
        if self.potion:
            protection += self.potion["effect"].get("protection", 0)
        return protection


    def __str__(self):
        return (f"name: {self.name}, "
                f"power: {self.power}, "
                f"hp: {self.hp}, "
                f"armour: {self.armours}, "
                f"weapon: {self.weapon}, "
                f"potion: {self.potion}, ")