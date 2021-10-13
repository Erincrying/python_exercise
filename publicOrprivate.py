# # 共有的属性和方法通过点操作符访问
# class Person:
#   name = '人名'
# p = Person()
# print(p.name)

# 私有变量，通过添加两个下划线定义
class Person:
  __name = '人名'
  # 添加方法从内部进行访问
  def getPivateName(self):
    return self.__name
p = Person()


# # 无法从外部进行访问
# print(p.__name)

# # 通过调用方法从内部访问name属性
# print(p.getPivateName())

# 通过名字改编 name mangling 访问内部属性
print(p._Person__name)