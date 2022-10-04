name = "마린"
hp = 40
damage = 5

print(f"\n {name} 유닛 생성")
print(f"\n 체력{hp} 공격력{damage}")

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print(f"\n {tank_name} 유닛 생성")
print(f"\n 체력 : {tank_hp} 공격력 : {tank_damage}")

def attack(name, location, damage):
    print(f"\n {name} : {location} 방향으로 공격. 공격력 : {damage}")
    
attack(name, "1시", damage)
attack(tank_name, "2시", tank_damage)