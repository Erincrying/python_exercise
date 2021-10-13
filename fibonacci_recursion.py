# 递归实现斐波那契数列
print('递归实现斐波那契数列')
def fab(n):
  if n < 1:
    print('输入有误')
    return -1
  
  if n == 1 or n == 2:
    return 1
  else:
    return fab(n-1) + fab(n-2)

number = int(input('请输入寻找的第几个斐波那契数列对应数据：'))
result = fab(number)
if result != -1:
  print('第%d个斐波那契数列对应的数据为%d' % (number, result))