'''
Author: your name
Date: 2020-11-07 17:14:57
LastEditTime: 2020-11-07 17:50:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vscode\study\03.pyddd
'''



class Player:
    def __init__(self,name):
        self.health = 100
        self.name = name
    def __str__(self):
        return f"{self.name}剩余{self.health}生命值"

#ddd
class Police(Player):
        def damage(self, target,damage = 50, ):
            target.health -= damage
            if target.health >= 0:

                print(f"{target.name}剩余{target.health}生命值")



class T(Player):
        def damage(self,  target,damage = 10,):
            target.health -= damage
            if target.health >= 0:
                print(f"{target.name}剩余{target.health}生命值")


def main():
        
    p1 = Police("p1")
    t1 = T("t1")
    t2 = T("t2")
    t3 = T("t3")
    ts = [t1,t2,t3]
    alives = ts
    while True :
        if p1.health > 0 :
            for tt in ts:
                p1.damage(tt)
                while tt.health >0 :
                    
                    for a in alives:
                        a.damage(p1)
                    p1.damage(tt)
                alives.remove(tt)
                if not alives:
                    print("反恐精英胜利")
                    break  
                
            
            
        else:
            print("反恐精英阵亡")
            break
  
            
if __name__ == "__main__":
    main()
