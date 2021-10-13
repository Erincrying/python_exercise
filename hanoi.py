print('汉诺塔解法')
def hanoi(n, x, y, z):
  if n == 1:
    print(x, '-->', z)
  else: 
    hanoi(n-1, x, z, y) # 将前n-1个盘子从x移动到y
    print(x, '-->', z) # 将最下面的盘子从x移动到z
    hanoi(n-1, y, x, z) # 将y上的n-1个盘子移动到z

n = int(input('请输入汉诺塔层数：'))
hanoi(n, 'X', 'Y', 'Z')