class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동 속도 : {2}".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]"
        .format(self.name, location, self.damage))
    def damaged (self, damage):
        print("{0}: {1} COX g."
        .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다."
        .format(self.name, self.hp))
        
        if self.hp <= 0:
            print("{0}: 파괴".format(self.name))
    def move(self, location):
        super().move(location)
        print("공격 유닛 입니다")
marine1 = AttackUnit("마린", 40, 5, 25)
marine1.move("5시")