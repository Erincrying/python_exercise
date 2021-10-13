# try_finally捕获异常

try:
  # 以写入的方式创建文件
  file = open('不存在的文件.txt', 'w')
  # 文件写入内容
  print(file.write('写入内容'))
  # 加法会报错，异常出现在打开文件之后
  sum = 1 + '1'
# 提示出错
except (OSError, TypeError) as reason:
  print('出错！错误的原因是' + str(reason))
# 通过finally运行必须要做的语句
finally:
  file.close()