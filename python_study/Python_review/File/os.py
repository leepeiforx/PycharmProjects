# 文件和文件夹操作

import os.path

# os模块
import os

'''
python标准库的os模块除了提供使用操作系统功能和访问文件系统的简便方法之外,还提供了大量文件与文件夹操作的方法
    access(path,mode)      测试是否可以按照mode指定的权限访问文件
    chdir(path)            把path设为当前工作目录
    chmod(path,mode,*,dir_fd=None,follow_symlinks=True)     改变当前文件的访问权限
    curdir                 当前文件夹
    environ                包含系统环境变量和值的字典     
    extsep                 当前操作系统所使用的文件扩展名分隔符
    get_exec_path()        返回可执行文件的搜索路径    
    getcwd()               返回当前工作目录
    listdir(path)          返回path目录夏的文件和目录列表
    mkdir(path[,mode=0777]) 创建目录,要求上级目录必须存在
    makedirs(path1/path2...,mode=511)   创建多级目录 ,会根据需要自动创建中间缺失的目录
    open(path,flags,mode=0o777,*,dir_fd=None)   按照mode指定的权限打开文件,默认权限为可读,可写,可执行
    popen(cmd,mode='r',buffering=-1)    创建进程,启动外部程序
    rmdir(path)             删除目录,目录中不能有文件或子文件夹
    remove(path)            删除指定的文件,要求用户拥有删除文件的权限,并且文件没有只读或其他特殊属性
    removedirs(path1/path2...)  删除多级目录,目录中不能有文件
    rename(src,dst)         重命名文件或目录,可以实现文件的移动,若目标文件已存在则抛出异常,不能跨越磁盘或分区
    replace(old,new)        重命名文件或目录,若目标文件已存在则直接覆盖,不能跨越磁盘或分区
    scandir(path='')        返回包括指定文件夹所有DirEntry对象的迭代对象,遍历文件夹时比listdir()更加高级
    sep                     当前操作系统所使用的路径分隔符
    startfile(fillpath[,operation]) 使用关联程序打开指定文件或启动指定应用程序
    stat(path)              返回文件的所有属性
    system()                启动外部程序
    truncate(path,length)   将文件截断,只保留指定长度的内容
    walk(top,topdown=True,onerror=None)     遍历目录树,该方法返回一个元组,包括3个元素,所有路径名,所有目录列表与文件列表
    write(fd,data)          将bytes对象data写入文件fd
'''

# os的基本用法

# 文件删除与文件重命名
# lantern_path = r'C:\Users\my_c\AppData\Roaming\Lantern'
# for fname in os.listdir(lantern_path):
#     if fname == '.lantern.exe.old':
#         os.remove(lantern_path + r'\lantern.exe')
#         os.rename(lantern_path + r'\.lantern.exe.old', lantern_path + r'\lantern.exe')

# os.getcwd()  # 返回当前的工作目录
# os.mkdir(os.getcwd() + r'\temp')
# os.chdir(os.getcwd() + r'\temp')  # 改变当前工作目录
# os.getcwd()
# os.mkdir(os.getcwd() + r'\test')
# os.listdir('.')
# os.rmdir('test')
# os.listdir('.')
# os.environ.get('path')  # 获取系统变量path的值

lantern_path = r'C:\Users\my_c\AppData\Roaming\Lantern'
import time

# time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.stat(lantern_path + r'\lantern.exe').st_ctime))  # 查看文件创建时间
# re_m_path = r'C:\Program Files (x86)\Regex Match Tracer\MTracer.exe'
# os.startfile(re_m_path)     # 启动MTracer.exe程序

# 下面的代码使用os模块的scandir()输出指定路径文件夹中所有扩展名为py的文件
wk_path = r'C:\Users\my_c\PycharmProjects\projects'
for entry in os.scandir(path=wk_path):
    if entry.is_file and entry.name.endswith('py'):
        print(entry.name)

# 如果需要遍历制定目录下所有子目录和文件,可以使用递归方法
from os import listdir
from os.path import join, isfile, isdir


def listDepthFirst(directory):
    '''
    深度优先遍历文件夹
    遍历文件夹,如果是文件就直接输出
    如果是文件,就输出显示,然后递归遍历该文件夹
    :param directory:
    :return:
    '''
    for subPath in listdir(directory):
        path = join(directory, subPath)
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listDepthFirst(path)


# listDepthFirst(wk_path)


# 下面的代码使用广度优先遍历方法

def listDirWidthFisrt(directory):
    '''
    广度优先遍历文件夹
    :param directory:
    :return:
    '''
    # 使用列表模拟双端队列,效率稍微受影响,不过关系不大
    dirs = [directory]

    # 如果还没遍历过文件夹,继续循环
    while dirs:
        # 遍历还没遍历过的第一项
        current = dirs.pop(0)
        # 遍历该文件夹,如果是文件就直接输出显示
        # 如果是文件夹,输出显示后,标记为待遍历项
        for subPath in listdir(current):
            path = join(current, subPath)
            if isfile(path):
                print(path)
            elif isdir(path):
                print(path)
                dirs.append(path)


# listDirWidthFisrt(wk_path)


# 或者,可以使用os模块的walk()方法指定文件夹内容的遍历

def visitDir(path):
    if not os.path.isdir(path):
        print('Error:', path, 'is not a directory or does not exist.')
        return
    list_dirs = os.walk(path)

    for root, dirs, files in list_dirs:  # 遍历该元组的目录和文件信息
        for d in dirs:
            print(os.path.join(root, d))  # 获取完整路径
        for f in files:
            print(os.path.join(root, f))  # 获取文件的绝对路径


visitDir(wk_path)

"""也可以使用glob()模块提供的功能实现类似的功能.另外,函数walk()的参数topdown默认值为True,表示从上到下遍历.在使用
rmdir()删除文件夹时要求文件夹必须为空,所以在递归删除指定文件夹中所有内容时影从下往上进行删除,此时可以将参数topdown设置
为False"""
# for root, dirs, files in os.walk(wk_path, topdown=False):
#     for name in files:
#         os.remove(os.path.join(root, name))
#     for name in dirs:
#         os.rmdir(os.path.join(root, name))


# %%
# os.path 模块
'''os.path模块提供了大量用于路径判断,切分,连接以及文件夹遍历的方法'''

'''
os.path.abspath(path)       返回给定路径的绝对路径
basename(path)              返回指定路径的最后一个组成部分
commonpath(paths)           返回给定多个路径的最长公共路径
commonprefix(paths)         返回给定的多个路径的最长公共前缀
dirname(p)                  返回给定路径的文件夹部分
exists(path)                判断文件是否存在
getatime(filename)          返回文件的最后访问时间
getctime(filename)          返回文件的创建时间
getmtime(filename)          返回文件的最后修改时间
getsize(filename)           返回文件的大小
isabs(path)                 判断路径是否是绝对路径
isdir(path)                 判断path是否为文件夹
isfile(path)                判断路径是否为文件
join(path,*paths)           连接两个或多个path
realpath(path)              返回给定路径的绝对路径
relpath(path)               返回给定路径的相对路径,不能跨越磁盘驱动器或分区
samefile(f1,f2)             测试f1和f2这两个路径是否引用同一个文件
split(path)                 以路径的最后一个斜线为分隔符把路径分割成两部分,以列表形式返回
splitext(path)              从路径中分隔文件的拓展名
splitdrive(path)            从路径中分隔驱动器的名称
'''
path = r'C:\Users\my_c\AppData\Roaming\Lantern'
os.path.dirname(path)  # 返回路径的文件夹名
os.path.basename(path)  # 返回路径的最后一个组成部分

path = r'C:\Users\my_c\AppData\Roaming\Lantern'
os.path.split(path)  # 切分文件路径和文件名

os.path.split('')  # 切分结果为空字符串
os.path.split('c:\\windows')  # 以最后一个斜线为分隔符
os.path.splitdrive(path)  # 切分驱动器符号
os.path.splitext(path)  # 切分文件扩展名
os.path.commonpath([r'c:\windows\notepad.exe', r'c:\windows\system'])  # 返回路径中的共同部分
os.path.commonprefix([r'a\b\c\d', r'a\b\c\e'])  # 返回字符串的最长公共前缀
os.path.realpath('tttt.py')  # 返回绝对路径
os.path.abspath('tttt.py')  # 返回绝对路径
os.path.relpath(path)  # 返回相对路径
os.path.relpath(path, 'dlls')  # 指定相对路径的基准位置

# %%
# shutil模块
'''
shutil模块常用方法
    copy(src,dst)        复制文件,新文件具有同样的文件属性,如果目标文件已存在则抛出异常
    copy2(src,dst)       复制文件,新文件具有同样的文件属性,包括创建时间,修改时间和最后访问时间,如果目标文件已存在则抛出异常
    copyfile(src,dst)    复制文件,不复制文件属性,如果目标文件存在则直接覆盖
    copyfileobj(fsrc,fdst) 在两个文件对象之间复制数据,例如conpyfileobj(open('123.txt'),open('456.txt','a'))
    copymode(src,dst)    把src的模式(mode bit)复制到dst上,之后两者具有相同的模式
    copystat(src,dst)    把src的模式位,访问时间等所有状态都复制到dst上
    copytree(src,dst)    递归复制文件夹
    disk_usage(path)     查看磁盘使用情况
    move(src,dst)        移动文件或递归移动文件夹,也可以给文件或文件夹重命名
    rmtree(path)         递归删除文件夹
    make_archive(base_name,format,root_dir=None,base_dir=None)  创建TAR或ZIP格式的压缩文件
    unpack_archive(filename,extract_dir=None,format=None)       解压缩文件夹
    
'''
import shutil

path = r'C:\Users\my_c\AppData\Roaming\Lantern'
shutil.copyfile(path + r'\uninstall_url.txt', path + r'\uninstall_url_new.txt')

# 将uninstall_url_new.txt,压缩至path文件夹
shutil.make_archive(path + r'\a.', 'zip', path, 'uninstall_url_new.txt')

# 解压缩
shutil.unpack_archive(path + r'\a.zip', path)

# 删除刚才解压缩的文件
# shutil.rmtree(path + r'\temp')

'''python标准库shutil的rmtree()还支持更多的参数,例如,可以使用onerror参数指定回调函数来处理删除文件
或文件夹失败的情况'''
import stat


def remove_readonly(func, path, _):  # 定义回调函数
    os.chmod(path, stat.S_IWRITE)  # 删除文件的只读属性
    func(path)


# shutil.rmtree(path + r'\temp')  # 文件有个只读文件,删除失败

# shutil.rmtree(path + r'\temp', onerror=remove_readonly)

# 使用shutil的conpytree()函数递归复制文件夹,并忽略扩展名为txt的文件加和"新"开头的文件和文件夹
# from shutil import copytree, ignore_patterns
#
# copytree(path, r'D:\lantern', ignore=ignore_patterns('*.txt', '新*'))

# %%
# 其他常用模块
# glob模块
'''glob提供了一些与文件搜索或便利有关的函数,并且允许使用命令行的通配符进行模糊搜索,更急灵活,方便'''
import glob

glob.glob('*.txt')  # 搜索当前文件夹中所有拓展名为txt的文件列表
glob.glob('?.*')  # 返回主文件名只有一个字符或数字的文件列表
glob.glob('[123abc]*.*')  # 返回当前文件夹中以1,2,3,a,b,c这几个字母开头的文件
glob.glob(r'H:\下载\*.*')  # 返回H:\下载 文件夹中所有文件列表
items = glob.iglob(r'H:\下载\*.*')  # 返回包含指定文件夹中所有文件的生成器对象
# for item in items:
#     print('P',item)
glob.glob(r'D:\STUDYING\**\*.pdf', recursive=True)  # 查找STUDYING文件夹中所有Pdf文件

# items = glob._rlistdir(r'D:\STUDYING', dironly=False)  # 遍历指定文件夹中所有文件,返回生成器对象
# for item in items:
#     print(item)

glob.glob1(r'H:\下载', '*.pdf')  # 返回指定文件夹中指定类型的文件列表
for i in glob._glob2(r'H:\下载', '**', dironly=True):  # 递归遍历指定文件夹下的所有文件
    print(i)

# %%
# fnmatch模块
'''该模块提供了文件名的检查功能,支持通配符的使用,其中通配符*可以匹配任意字符,"?"可以匹配任意单个字符,[seq]可以匹配seq中的任意字符
[!seq]可以匹配任何不属于seq的字符
    标准库fnmatch提供的fnmatch(filename,pattern)函数用来检查文件名是否与模式pattern匹配,返回True或False,
    fnmatachcase(filename,pattern)完成相似的功能,区别在于该函数区分大小写'''

import fnmatch

path = r'C:\Users\my_c\AppData\Roaming\Lantern\lantern.exe'
fnmatch.fnmatch(path, '*.exe')
fnmatch.fnmatch(r'lantern.exe', '???????.eXe')
fnmatch.fnmatchcase(r'lantern.exe', '???????.eXe')
fnmatch.fnmatchcase(r'lantern.exe', '???????.exe')

'''标准库fnmatch提供的filiter(names,pattern)函数用来返回names中符合pattern的那部分元素构成的列表
等价与[n for n in names if fnmatch(n,pattern)],但效率更高'''
fnmatch.filter(os.listdir(r'C:\Users\my_c\PycharmProjects\projects'), "*.py")
