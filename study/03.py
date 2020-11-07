


class Player:
    def __init__(self,name):
        self.health = 100
        self.name = name


#ddd
class Police(Player):
        def damage(self, damage, target):
            target.health -= damage
            if target.health <= 0:
                print(f'目标{target}死亡。')
            print(f"{target.name}剩余{target.health}生命值")



class T(Player):
        def damage(self, damage, target):
            target.health -= damage
            if target.health <= 0:
                print(f'目标{target}死亡。')
            print(f"{target.name}剩余{target.health}生命值")



p1 = Police("p1")
t1 = T("t1")
t2 = T("t2")
t3 = T("t3")

p1.damage(10, t2)
p1.damage(10, t2)
p1.damage(10, t2)
