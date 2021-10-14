# 组合（将需要的类一起进行实例化并放入新的类中）
# 现在要求定义一个类，叫水池，水池里要有乌龟和鱼。
class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池里一共有乌龟 %d 条,鱼 %d 条' % (self.turtle.num, self.fish.num)) # self.turtle是Turtle实例化后的对象

pool = Pool(1, 10)
pool.print_num()
