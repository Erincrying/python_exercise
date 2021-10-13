# else搭配循环使用
def showMaxFactor(num):
  count = num // 2 # 整除
  while count > 1:
    if num % count == 0:
      print('%d的最大公约数是%d' %(num, count))
      break # 直接跳出循环
    count -= 1
  # else搭配while使用
  else:
    print('%d是素数！' % num)

num = int(input('请输入一个整数：'))
showMaxFactor(num)