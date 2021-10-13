print('break用法')
bingo = '天才'
answer = input('请输入答案词语：')

while True:
  if bingo == answer:
    break
  answer = input('答案错误，请再次输入：')

print('输入正确')