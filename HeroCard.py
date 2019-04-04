cards = [
    {"name":"斧王","types":["兽人","战士"],"atk":100,"ftk":100,"cost":1},
    {"name":"巨牙海民","types":["野兽","兽人"],"atk":100,"ftk":100,"cost":1},
    {"name":"魅惑魔女","types":["野兽","德鲁伊"],"atk":100,"ftk":100,"cost":1},
    {"name":"赏金猎人","types":["地精","刺客"],"atk":100,"ftk":100,"cost":1},
    {"name":"食人魔魔法师","types":["食人魔","法师"],"atk":100,"ftk":100,"cost":1},
    {"name":"蝙蝠骑士","types":["巨魔","骑士"],"atk":100,"ftk":100,"cost":1},
    {"name":"敌法师","types":["精灵","恶魔猎手"],"atk":100,"ftk":100,"cost":1},
    {"name":"发条技师","types":["工匠","地精"],"atk":100,"ftk":100,"cost":1},
    {"name":"水晶室女","types":["人类","法师"],"atk":100,"ftk":100,"cost":2},
    {"name":"树精","types":["精灵","德鲁伊"],"atk":100,"ftk":100,"cost":2},
    {"name":"剑圣","types":["兽人","战士"],"atk":100,"ftk":100,"cost":2},
    {"name":"兽王","types":["兽人","猎人"],"atk":100,"ftk":100,"cost":2},
    {"name":"伐木机","types":["地精","工匠"],"atk":100,"ftk":100,"cost":2},
    {"name":"影魔","types":["恶魔","术士"],"atk":100,"ftk":100,"cost":3},
    {"name":"狼人","types":["战士","人类"],"atk":100,"ftk":100,"cost":3},
    {"name":"闪电幽魂","types":["元素","法师"],"atk":100,"ftk":100,"cost":3},
    {"name":"剧毒术士","types":["野兽","术士"],"atk":100,"ftk":100,"cost":3},
    {"name":"风行者","types":["精灵","猎人"],"atk":100,"ftk":100,"cost":3},
    {"name":"光之守卫","types":["人类","法师"],"atk":400,"ftk":100,"cost":4},
    {"name":"末日使者","types":["恶魔","战士"],"atk":400,"ftk":100,"cost":4},
    {"name":"圣堂刺客","types":["刺客","精灵"],"atk":400,"ftk":100,"cost":4},
    {"name":"龙骑士","types":["人类","龙","骑士"],"atk":400,"ftk":100,"cost":4},
    {"name":"利爪德鲁伊","types":["野兽","德鲁伊"],"atk":400,"ftk":100,"cost":4},
    {"name":"矮人直升机","types":["工匠","矮人"],"atk":400,"ftk":100,"cost":5},
    {"name":"巫妖","types":["亡灵","法师"],"atk":400,"ftk":100,"cost":5},
    {"name":"潮汐猎人","types":["猎人","娜迦"],"atk":400,"ftk":100,"cost":5},
    {"name":"谜团","types":["术士","元素"],"atk":400,"ftk":100,"cost":5},
    {"name":"地精工程师","types":["地精","工匠"],"atk":400,"ftk":100,"cost":5},
]


class HeroCard:
    def __init__(self,id,name,types,atk,ftk,cost):
        self.id = id
        self.name = name
        self.types = types
        self.atk = atk
        self.ftk = ftk
        self.cost = cost
        self.level = 1
    def to_string(self):
        return f'id is {self.id} name is {self.name}; types are {self.types}; atk is {self.atk}; ftk is {self.ftk}; cost is {self.cost} ammount is {self.ammount}'

    def reduce_ammount(self):
        self.ammount = self.ammount - 1

    def add_ammoun(self,ammount):
        self.ammount = self.ammount + ammount
def init_cards():
    herocards = []
    id = 1
    for card in cards:
        herocard = HeroCard(id = id,name=card['name'], types=card['types'], atk=card['atk'], ftk=card['ftk'], cost=card['cost'])
        herocards.append(herocard)
        id = id+1
    return herocards





