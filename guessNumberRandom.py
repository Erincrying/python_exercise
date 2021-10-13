print('猜随机数')
import random
secret = random.randint(1,10)
temp = input('猜数字：')
guess = int(temp)
while guess != secret:
  temp = input('猜错了重新输入：')
  guess = int(temp)
  if guess == secret:
    print('yes')
  else: 
    if guess > secret: 
      print('大了')
    else: 
      print('小了')
print('游戏结束')