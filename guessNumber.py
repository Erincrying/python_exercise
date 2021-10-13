temp = input('猜数字：')
guess = int(temp)
if guess == 8:
  print('yes')
else: 
  if guess>8: 
    print('大了')
  else: 
    print('小了')

print('游戏结束')
