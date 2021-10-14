# 类、类对象和实例对象，修改类对象的属性不会修改实例对象的属性
class C:
  count = 0

a = C()
b = C()
c = C()

print("a,b,c实例化C后的count初始值为", a.count ,b.count, c.count)

# 修改实例化对象的属性
c.count += 10
print("实例化对象c.count做加法后a,b,c的值", a.count ,b.count, c.count)
# 修改类对象的属性
print("C类对象的count值", C.count)
C.count += 100
print("类对象C.count做加法后a,b,c的值", a.count ,b.count, c.count)
