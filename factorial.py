# 求阶乘
def factorial(n):
  result = n
  for i in range(1, 10):
    result *= i

  return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print('%d的阶乘是%d' % (number, result))