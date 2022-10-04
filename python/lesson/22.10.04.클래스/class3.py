class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛 생성".format(self.name))
        print(f"체력: {self.hp}, 공격력: {self.damage}")
# marin1 = Unit("마린", 40, 5)
# marin1 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wrait1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wrait1.name, wrait1.damage))
wrait2 = Unit("빼앗은 레이스", 80, 5)
wrait2.clocking = True

if wrait2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다".format(wrait2.name))