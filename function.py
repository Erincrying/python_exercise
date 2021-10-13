def discounts(price, rate):
  final_price = price * rate
  # 如果在函数内试图修改全局变量，局部函数内python会自动创建一个新的局部变量（局部范围内不能直接修改全局变量）
  # 这里如果实在想改变全局变量可以 global old_price
  # old_price = 50，通过global声明变量进行重新赋值
  old_price = 50
  print('函数内修改全局变量的值：', old_price)
  return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣：'))
new_price = discounts(old_price, rate)
print('全局范围内展示全局变量的值：', old_price)
print('打折后的价格是', new_price)