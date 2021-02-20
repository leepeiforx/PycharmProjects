# 常见异常表现形式
# 2/0     # 除0错误
# 'a' + 2     # 操作数类型不支持
# {3, 4, 5} * 3  # 操作数类型不支持
# print(testStr)  # 变量名不存在
# fp = open(r'D:\windoesltxt', 'rb')      # 文件不存在
# len(3)          # 参数类型不匹配
# list(3)         # 参数类型不匹配


#%%
# 异常处理结构
# 1.try...except...
"""
    如果try子语句中的代码引发异常并被except捕获,就执行except字句的代码块;
    如果try中的代码块没有出现异常就继续往下执行异常处理结构后面的代码,如果出现异常但未
    被except捕获,继续往外层抛出;如果所有层都没有捕获并处理该异常,程序崩溃并将该异常呈现给最终用户
"""
# try:
#     #  可能引起异常的代码,先执行一下试试
# except Exception[as reason]:
    #  如果try中的代码抛出异常并被except捕捉,就执行这里的代码

# while True:
#     x = input('Please input')
#     try:
#         x = int(x)
#         print('you have input {}'.format(x))
#         break
#     except Exception as e:
#         print('Error')


#2.try...except...else
'''带有else字句的异常处理结构可以看作是一种特殊的双分支选择结构,如果try中的代码抛出了异常并且被except语句捕捉则执行
相应的异常处理代码,这种情况下就不执行else中的代码;如果try中的代码没有引发异常,则执行else块的代码'''

# try:
# #   可能会引发异常的代码
# except Exception [as reason]:
# #   用来处理异常的代码
# else:
#     如果try字句的代码没有引发异常,就继续执行这里的代码

# while True:
#     x = input('Please input')
#     try:
#         x = int(x)
#     except Exception as e:
#         print('Error')
#     else:
#         print('You have input {}'.format(x))
#         break

# 3. try...except...finally
'''无论try中的代码是否发生异常,也不管抛出的异常有没有被except捕获,finally子句中的代码总是会得到执行'''
# try:
# #   可能会引发异常的代码
# except Exception [as reason]:
# #   用来处理异常的代码
# finally:
#     无论try子句中的代码是否引发异常,都会执行这里的代码

def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('The second parameter cannot be 0.')
    finally:
        print(-1)

# div(3, 0)

'''如果try子句中的异常没有被except语句捕获和处理,或者except子句或else子句中的代码抛出了异常,那么这些异常
在finally子句执行完后再次抛出'''

# div(3,'5')

'''需要注意的是,异常处理结构不是万能的,并不是采用了异常处理结构就万事大吉,finally子句中的代码也可能会引发异常'''

# try:
#     f1 = open('text1.text','r') # 文件不存在,抛出异常,不会创建文件对象f1
#     line = f1.readline()    # 后面的代码不会执行
#     print(line)
# except SyntaxError:         # 这个except并不能捕捉上面的异常
#     print('sth wrong')
# finally:
#     f1.close()              # f1不存在,再次引发异常
#

'''如果在函数中使用异常处理结构,尽量不要在finally子句中使用return语句,一面法师非常难以发现的逻辑错误'''

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'The second parameter cannot be 0'
    finally:
        return 'Error'

print(div(3,5))
print(div(3,0))

# 4.可以捕捉多种异常的异常处理结构
'''该结构类似于多分枝选择结构'''
# try:
#   可能会引发异常的代码
# except Exception1:
#     用来处理异常1的代码
# except Exception2:
#     用来处理异常1的代码
# except Exception3:
#     用来处理异常3的代码
# except Exception4:
#     用来处理异常4的代码

# try:
#     x = float(input('请输入被除数:'))
#     y = float(input('请输入除数'))
#     z = x / y
# except ZeroDivisionError:
#     print('除数不能为0')
# except ValueError:
#     print('被除数和除数应为数值类型')
# except NameError:
#     print('变量不存在')
# else:
#     print('x / y =',z)

'''为了减少代码量,python允许把多个异常类型放在一个元组中,然后用一个except子句同时捕捉多种异常'''

# try:
#     x = float(input('请输入被除数:'))
#     y = float(input('请输入除数'))
#     z = x / y
# except (ZeroDivisionError,ValueError,NameError):
#     print('出现异常')
# else:
#     print('x / y =',z)

#5.同时包含else子句,finally子句和多个except子句的异常处理结构
def div(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except ValueError:
        print('ValueError')
    else:
        print('No Error')
    finally:
        print('executing finally clause')

div(3,4)

#%%
# 断言与上下文管理语句
'''断言语句assert常用来在程序的某个位置确认某个条件必须满足.一般只在开发和测试阶段使用'''
a = 3
b = 5
# assert a == b   #a must be equal to b
# try:
#     a == b
# except AssertionError as reason:
#     print('Error')
#     print(reason.__class__.__name__)
#     print(reason)

