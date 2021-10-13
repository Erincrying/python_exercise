#任务：将文件（talk.txt）中的数据进行分割并按照以下规律保存起来：

#–A作者的对话单独保存为A_*.txt的文件（去掉“A作者:”）

#–B作者的对话单独保存为B_*.txt的文件（去掉“B作者:”）

#–文件中总共有三段对话，分别保存为A_1.txt, B_1.txt，A_2.txt, B_2.txt, A_3.txt, B_3.txt共6个文件（提示：文件中不同的对话间已经使用“==========”分割）

f = open('talk.txt','r', encoding='UTF-8')

listA = []
listB = []
count = 1

for each_line in f:
  if each_line[:6] != '======': # 切割前几个等号即可
     (role,line_spoken) = each_line.split('：',1) # split以:进行字符切割，切割一次，这里注意txt中的符号是中文符号还是英文符号
     # 将切得到的两部分内容依次存放在role与line_spoken中
     if role == 'A作者':
       listA.append(line_spoken) # A作者的内容添加到列表A中
     if role == 'B作者':
       listB.append(line_spoken) # B作者的内容添加到列表B中
  else:
    # 遇到等号，进行文件保存操作
    file_name_A = 'A_' + str(count) + '.txt'
    file_name_B = 'B_' + str(count) + '.txt'
    
    A_file = open(file_name_A,'w') # 以w模式新建一个以file_name_A命名的txt文件
    B_file = open(file_name_B,'w') # 并贴上B_file的标签

    A_file.writelines(listA) # 将列表A中的内容写入到A_file文件中
    B_file.writelines(listB)

    A_file.close() # 关闭A_file文件
    B_file.close()

    listA = [] # 清空列表
    listB = []
    count += 1

  # 循环是以等号为判断条件，这样的话，最后一段文字结束没有等号的话，需要单独对最后一段文字进行处理（处理方法直接重复调用上述else部分）
  file_name_A = 'A_' + str(count) + '.txt'
  file_name_B = 'B_' + str(count) + '.txt'
  
  A_file = open(file_name_A,'w') # 以w模式新建一个以file_name_boy命名的txt文件
  B_file = open(file_name_B,'w') # 并贴上B_file的标签

  A_file.writelines(listA) # 将列表A中的内容写入到A_file文件中
  B_file.writelines(listB)

  A_file.close() # 关闭A_file文件
  B_file.close()

f.close()