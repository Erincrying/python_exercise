# with用法
try:
  with open('data.txt', 'w') as file:
    for eachLine in file:
      print(eachLine)
except OSError as reason:
  print('出现错误！原因是' + str(reason))
# 不需要finally

# 普通用法
# try:
#   file = open('data.txt', 'w') # 试图打开一个不存在的文件
#   for eachLine in file:
#     print(eachLine)
# except OSError as reason:
#   print('出现错误！原因是' + str(reason))
# finally:
#   file.close()
