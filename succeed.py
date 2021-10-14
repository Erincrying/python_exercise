# 继承：一个子类可以继承它的父类的所有属性和方法
class Parent:
  def hello(self):
    print('调用父类的hello方法')

# 一个子类可以继承它的父类的所有属性和方法
# class DerivedClassName(BaseClassName):
# class Child(Parent):
#   pass # 直接向下执行

# 如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法和属性（即子类方法属性改变，父类是不变的
class Child(Parent):
  def hello(self):
    print('调用子类的hello方法')

p = Parent()
c = Child()

p.hello()
c.hello()

