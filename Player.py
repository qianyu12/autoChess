from auto_chess.Game import Game


class Player:
    def __init__(self):
        self.population = 1
        self.on_field_population = 0
        self.level = 1
        self.exp = 0
        #最大为10个
        self.on_field_heroes = []
        #最大为8个
        self.back_field_heroes = []
        self.money = 1
        #胜利额外+1
        #三连胜+1，四连胜+2，五连胜及以上+3
        #利息：持有财产的0.1，最高5

    def add_back_field_heroes(self,hero_card):
        self.back_field_heroes.append(hero_card)

    def del_back_field_hero(self,hero_card):
        self.back_field_heroes.remove(hero_card)

    def add_on_field_heroes(self,hero_card):
        self.on_field_heroes.append(hero_card)

    def del_on_field_heroes(self,hero_card):
        self.on_field_heroes.remove(hero_card)

    def add_money(self,num):
        self.money = self.money + num

    def sub_money(self,num):
        self.money = self.money - num