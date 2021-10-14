
import random as r

# 鱼的大类
class Fish:
  def __init__(self):
      self.x = r.randint(0, 10)
      self.y = r.randint(0, 10)
  def move(self):
      self.x -= 1
      print("目前的位置是", self.x, self.y)

# 金鱼
class Goldfish(Fish):
    pass
# 鲤鱼
class Garp(Fish):
    pass
# 三文鱼
class Salmon(Fish):
    pass
# 鲨鱼
class Shark(Fish):
# 这里重写了方法，会把父类当中的方法覆盖掉，导致无法获取x、y的属性
  def __init__(self):
      # 规避未定义问题
    #   #（1）调用未绑定的父类方法
    #   Fish.__init__(self) # 调用父类的方法，但是这里的self还是指向子类，相当于Fish.__init__(shark)
      #（2）使用super函数
      super().__init__()
      self.hungry = True

  def eat(self):
      if self.hungry:
          print('继续吃')
          self.hungry = False
      else:
          print('吃不下')


fish = Fish()
goldfish = Goldfish()
shark = Shark()
# 移动
fish.move()
goldfish.move() # 继承父类的方法
shark.eat() # 调用子类的方法

shark.move()
