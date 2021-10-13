# try_except捕获异常

try:
  # 转换出错
  # int('abc')
  # 加法会报错
  sum = 1 + '1'
  file = open('不存在的文件.txt')
  print(file.read())
  file.close()
# 操作系统方面的异常
# except OSError:
#   print('文件出错！')
# 输出原因
# except OSError as reason:
#   print('文件出错！\n错误的原因是' + str(reason))
# # 多个except
# except TypeError as reason:
#   print('类型出错！\n错误的原因是' + str(reason))
# 包含所有报错，不指定特定报错
# 上面两个异常捕获也可以写成下面的样子
except (OSError, TypeError) as reason:
  print('出错！错误的原因是' + str(reason))
# 统一提示出错
# except:
#   print('出错！')
