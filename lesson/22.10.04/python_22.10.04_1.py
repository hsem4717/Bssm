class human:
    def __init__(self, height, age):
        self.height = height
        self.age = age
    def how_old(self):
        print(self.age, "살 입니다")
        
    def how_tall(self):
        print(self.height, "cm 입니다")
        
sunah = human(166, 29)
eunwoo = human(185, 29)

sunah.how_old()
human.how_old(sunah)

eunwoo.how_tall()
print(sunah.height)