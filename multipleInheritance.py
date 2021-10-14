# 多重继承
class Base1:
  def foo1(self):
    print("Base1的foo1")

class Base2:
  def foo2(self):
    print("Base2的foo2")

# 多重继承
class C(Base1, Base2):
  pass

c = C()
c.foo1()
c.foo2()