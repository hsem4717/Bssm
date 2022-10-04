class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛 생성".format(self.name))
        print(f"체력: {self.hp}, 공격력: {self.damage}")
marin1 = Unit("마린", 40, 5)
marin1 = Unit("마린", 40, 5)
tank = Unit("탱크", 40, 5)