# else搭配异常捕获使用
try:
  # int('abc') # 类型错误
  int('123') # 类型未出错
  print(int('123'))
except ValueError as reason:
  print('出错了！错误原因是' + str(reason))
# else搭配异常捕获使用
else:
  print('没有出错')