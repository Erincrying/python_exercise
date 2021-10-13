# 迭代实现斐波那契数列
print('迭代实现斐波那契数列')
def fab(n):
  n1 = 1
  n2 = 1
  n3 = 1

  if n < 1:
    print('输入有误')
    return -1

  while (n-2) > 0:
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    n -= 1
  return n3

number = int(input('请输入寻找的第几个斐波那契数列对应数据：'))
result = fab(number)
if result != -1:
  print('第%d个斐波那契数列对应的数据为%d' % (number, result))