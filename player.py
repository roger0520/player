

class Player:
    def __init__(self, name, ap):
        print(name, '誕生了')
        self.name = name
        self.hp = 100
        self.ap = ap
    
    def attack(self, target):
        print(self.name, 'attacking', target.name)
        target.hp = target.hp - self.ap


player1 = input('請輸入玩家一的名字: ')
player2 = input('請輸入玩家二的名字: ')
p1 = Player(player1, 5)
p2 = Player(player2, 10)
p1.attack(p2)
print(p2.name, '生命值剩下: ', p2.hp)

