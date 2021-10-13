# 将list通过二进制写入文件，然后读取其二进制文件
import pickle
my_list = [123, 2.22, 'test', ['abc']]

# 通过写入二进制模式打开文件
pickle_file = open('mylist_pkl.pkl', 'wb')

# 序列化对象，将对象obj保存到文件file中去
pickle.dump(my_list, pickle_file)
# 关闭文件
pickle_file.close()

# 通过读取二进制模式打开文件
pickle_file = open('mylist_pkl.pkl', 'rb')

# 反序列化对象，将文件中的数据解析为一个python对象
my_list2 = pickle.load(pickle_file)

print(my_list2)