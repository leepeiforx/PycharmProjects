# import os
import os.path
import shutil
import glob

# #rename实现文件的重命名和移动
# # os.rename(r'C:\Users\Administrator\Desktop\da\map.csv',r'C:\Users\Administrator\Desktop\da\photos\pic\map.csv')
#
# #返回当前的工作目录
# print(os.getcwd())


#返回当前的工作目录
# os.getcwd()

#创建工作目录
# os.mkdir(os.getcwd()+'\\temp')
#改变工作目录
# os.chdir(os.getcwd()+'\\temp1')
# print(os.listdir('.'))
# print(os.environ.get('path'))           #获取系统变量path的值

path = r'C:\Users\Administrator\Desktop\da\test.txt'

print(os.path.dirname(path))              #返回路径的文件夹名

print(os.path.basename(path))             #返回路径的最后一个组成部分

print(os.path.split(''))                  #切分结果为空字符串

# print(help(os.path))

help(shutil)