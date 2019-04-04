import random
from functools import reduce

from auto_chess.HeroCard import init_cards
from auto_chess.Player import Player


class Game:
    def __init__(self):
        self.hero_cards = []
        self.draw_nums = 5
        self.turn = 1
        self.player  =  Player()

    def init_game(self):
        self.hero_cards = init_cards()
        for hero_card in self.hero_cards:
            if hero_card.cost == 1:
                hero_card.ammount = random.randint(20,25)
            elif hero_card.cost == 2:
                hero_card.ammount = random.randint(15,20)
            elif hero_card.cost == 3:
                hero_card.ammount = random.randint(12,15)
            elif hero_card.cost == 4:
                hero_card.ammount = random.randint(10,15)
            else:
                hero_card.ammount = 10

    #prob_interval->概率区间2->[30,100] or 3->[50,90,100],or4->[40,80,100] or 5->[35,70,92,100] or 6->[25,60,80,100]
    #or 7->[20,50,80,100] 8->[20,50,70,99,100] 9->[20,50,70,92,100] 10->[15,40,60,85,100]
    def rand_gen_give_cards(self,prob_interval):
        total = len(prob_interval)
        # 抽签结果
        lucky_numbers = []
        # 抽取数量
        numbers = [0 for x in range(total)]
        # 最终结果
        heroes_selected = []
        while (len(lucky_numbers) < self.draw_nums):
            temp = random.randint(1, 100)
            if temp not in lucky_numbers:
                lucky_numbers.append(temp)
            n = 0
            for x in prob_interval:
                if temp < x:
                    break
                else:
                    n = n + 1
            numbers[n] = numbers[n] + 1
        cost = 1
        for y in numbers:
            heroes_selected = heroes_selected + self.rand_choose_cards(cost=cost, n=y)
            cost = cost + 1
        for some_hero in heroes_selected:
            print(some_hero.to_string())
        return heroes_selected
    #cost为几费的卡牌，n为取的卡牌数量
    def rand_choose_cards(self,cost,n):
        cards = list(filter(lambda card:card.cost == cost,self.hero_cards))
        #返回的卡佩
        result = []
        #概率区间：
        probility_interval = []
        #选择的数字们
        lucky_nums = []
        #temp
        temp = 0
        for card in cards:
            temp += card.ammount
            probility_interval.append(temp)
        # 几费的总数量
        card_ammount = probility_interval[-1]
        print("card ammount" + str(card_ammount))
        while(len(result)<n):
            lucky_num = random.randint(1,card_ammount)
            if lucky_num not in lucky_nums:
                lucky_nums.append(lucky_num)
                start = 0
                for x in probility_interval:
                    if lucky_num <= x:
                        break
                    else:
                        start = start + 1
                result.append(cards[start])
        return result


    def gen_five_cards(self):
        #卡池
        hero_selected = []
        #2->[30,100] or 3->[50,90,100],or4->[40,80,100] or 5->[35,70,92,100] or 6->[25,60,80,100]
    #or 7->[20,50,80,100] 8->[20,50,70,99,100] 9->[20,50,70,92,100] 10->[15,40,60,85,100]
        #只能抽到1星
        poulation = self.player.population
        if(poulation == 1):
            hero_selected = self.rand_gen_give_cards([100])
        #2人口=>只能抽到1星或者2星=>1星概率为70，2星概率为30
        if(poulation == 2):
            hero_selected = self.rand_gen_give_cards([70,100])
        #3人口
        if(poulation == 3):
            hero_selected = self.rand_gen_give_cards([50,90,100])
        #4人口
        if(poulation == 4):
            hero_selected = self.rand_gen_give_cards([40,80,100])
        #5人口
        if(poulation == 5):
            hero_selected = self.rand_gen_give_cards([35,70,92,100])
        #6人口
        if (poulation == 6):
            hero_selected = self.rand_gen_give_cards([25,60,80,100])
        #7人口
        if (poulation == 7):
            hero_selected = self.rand_gen_give_cards([20,50,80,100])
        #8人口
        if (poulation == 8):
            hero_selected = self.rand_gen_give_cards([20,50,70,99,100])
        #9人口
        if (poulation == 9):
            hero_selected = self.rand_gen_give_cards([20,50,70,92,100])
        #10人口
        if (poulation == 10):
            hero_selected = self.rand_gen_give_cards([15,40,60,85,100])
        return  hero_selected

    #买英雄的时候还要减取money，0=》后台满了，1-》成功，-1=》没钱
    def draw_one_card(self,hero_card):
        if(self.player.money >= hero_card.cost):
            if(self.player.back_field_heroes==8):
                #后台满了
                return 0
            else:
                self.player.sub_money(hero_card.cost)
                #相应的库中数量-1,后台英雄数量+1
                for card in self.hero_cards:
                    if card.id == hero_card.id:
                        card.reduce_ammount()
                        self.player.add_back_field_heroes(card)
                        return 1

    #删除场上，或者后场的,is_on_field->是否在场？
    #得到钱，1星x费 =》x元 ；2星x费=》 3星x费=》
    #星*（费+1）-费
    #人口L：删除一星怪，数量+1；删除二星怪，数量加3，删除三星怪，数量加9
    def del_one_card(self,is_on_field,hero_card):
        if is_on_field:
            self.player.on_field_heroes.remove(hero_card)
        else:
            self.player.back_field_heroes.remove(hero_card)
        for card in self.hero_cards:
            if card.id == hero_card.id:
                #如果删除的登记为1
                if hero_card.level == 1:

                elif: hero_card.level == 2:

                else:






