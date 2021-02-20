class A:

    def __init__(self,value1=0,value2=0):   #构造方法
        self._value1 = value1
        self.__value2 = value2               #私有成员

    def setValue(self, value1, value2):       #成员方法,公有成员

        self._value1 = value1
        self.__value2 = value2              #在类内不可以直接访问私有成员

    def show(self):
        print(self._value1)
        print(self.__value2)

a = A()
a._value1                                   #在类外部可以直接访问非私有成员
# a.__value2
a._A__value2                                #在外部访问对象的私有数据成员(不建议这么做)


class create_class_num_limit():

    total = 0

    def __new__(cls, *args, **kwargs):      #该方法在__init__()之前被调用
        if cls.total >= 3:
            raise Exception('最多只能创建3个对象')
        else:
            return object.__new__(cls)

    def __init__(self):
        create_class_num_limit.total = create_class_num_limit.total+1

class Demo:
    pass
t = Demo()
def test(self,v):
    self.value = v
t.test = test                                      #动态增加普通函数
t.test(t,3)                                        #需要为self传递参数
print(t.value)

import types
t.test = types.MethodType(test,t)                  #动态增加绑定的方法
t.test(5)                                          #不需要为self传递参数
print(t.value)

class Root():

    __total = 0

    def __init__(self,v):                          #构造方法,特殊方法
        self.__value = v
        Root.__total += 1

    def show(self):
        print('self.__value:',self.__value)
        print('Root.__total',Root.__total)

    @classmethod                                   #修饰器,声明类方法
    def classShowTotal(cls):                       #类方法,一般以cls作为第一个参数的名字
        print(cls.__total)

    @staticmethod                                  #修饰器,声明静态方法
    def staticShowTotal():                         #静态方法,可以没有参数
        print(Root.__total)

r = Root(3)
r.classShowTotal()
r.staticShowTotal()
rr = Root(5)
Root.classShowTotal()                              #通过类名调用类方法
Root.staticShowTotal()                             #通过类名调用静态方法
# Root.show()                                      #试图通过类名直接调用实例方法,失败

Root.show(rr)

import abc
class Foo(metaclass=abc.ABCMeta):                  #抽象类
    def f1(self):
        print(123)
    def f2(self):
        print(456)

    @abc.abstractmethod                             #抽象方法
    def f3(self):
        raise Exception('You must reimplement this method.')

class Bar(Foo):
    def f3(self):                                   #必须重新实现基类中的抽象方法
        print(3333)

b =Bar()
b.f1()
b.f3()

class Test():

    def __init__(self,value):
        self.__value = value                        #私有数据成员

    @property                                       #修饰器,定义属性,提供对私有数据成员的访问
    def value(self):                                #只读属性,无法修改和删除
        return self.__value

t =Test(3)
# t.value = 5
# del t.value
print(t.value)


class Test_1():

    def __init__(self, value):
        self.__value = value                    # 私有数据成员

    def __get(self):                            # 读取私有数据成员的值
        return self.__value

    def __set(self, v):
        self.__value = v

    value = property(__get, __set)              # 可读可写属性,指定相应的读写方法

    def show(self):
        print(self.__value)


t_1 = Test_1(10)
print(t_1.value)
t_1.value = 3
t_1.show()
# del t_1.value


class Test_2():

    def __init__(self,value):
        self.__value = value

    def __get(self):
        return self.__value

    def __set(self,value):
        self.__value = value

    def __del(self):
        del self.__value

    value = property(__get, __set, __del)               #可读,可写,可删除的属性

    def show(self):
        print(self.__value)


t_2 = Test_2(1)
t_2.show()
t_2.value = 3
print(t_2.value)
del t_2.value
# t_2.show()


import types
class Car():
    price = 100000                                  #属于类的数据成员
    def __init__(self, c):
        self.color = c                              #属于对象的数据成员

car1 = Car('red')                                   #实例化对象
print(car1.color,Car.price)                         #访问对象和类的数据成员
Car.price = 999999                                  #修改类属性
Car.name = 'QQ'                                     #动态增加类属性
car1.color = 'Yellow'                               #修改实例属性

def setSpeed(self,s):
    self.speed = s

car1.setSpeed = types.MethodType(setSpeed,car1)     #动态为对象增加成员方法
car1.setSpeed(80)
print(car1.speed)

class Person():

    def __init__(self,name = '',age = 20,sex = 'male'):
        #通过调用方法进行初始化,这样可以诶对参数进行更好地控制
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self,name):
        if not isinstance(name,str):
            raise  Exception('name must be string.')
        self.__name = name

    def setAge(self,age):
        if type(age) != int:
            raise Exception('age must be an integer.')
        self.__age = age

    def setSex(self,sex):
        if sex not in ('famale','male'):
            raise Exception('sex must be "male" or "female". ')
        self.__sex = sex

    def show(self):
        print(self.__name, self.__age, self.__sex)


#派生类
class Teacher(Person):

    def __init__(self, name = '', age = 30,sex = 'male', department = 'Computer'):

        #调用基类构造方法初始化基类的私有数据成员
        super(Teacher, self).__init__(name,age,sex)
        #也可以这样初始化基类的私有数据成员
        #Person.__init__(self, name, age, sex)
        #初始化派生类的数据成员
        self.setDepartment(department)

    def setDepartment(self, department):
        if type(department) != str:
            raise Exception('department must be a string.')
        self.__department = department

    def show(self):
        super(Teacher, self).show()
        print(self.__department)


if __name__ == '__main__':
    #创建基类对象
    zhangsan = Person('zhangsan',19,'male')
    zhangsan.show()
    print('='*30)

    lisi = Teacher('li si',32,'male','math')
    lisi.show()

    #调用继承的方法修改年龄
    lisi.setAge(35)
    lisi.show()


class A():

    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private() method of A')

    def public(self):
        print('public() method of A')

    def __test(self):
        print('__test() method of A.')

class B(A):                                 #注意,B类没有构造方法

    def __private(self):
        print('__private() method of B')

    def public(self):
        print('public() method of B')

b =B()                                         #创建派生类对象
# b._B__test()                                #派生类没有继承基类中的私有成员方法
# b._A__test()                                #通过特殊方法可以访问基类中的私有成员方法
b._A__private()                               #没有严格意义的私有成员



class C(A):

    def __init__(self):                       #注意,C类存在构造方法
        self.__private()
        self.public()

    def __private(self):
        print('__private() method of C.')

    def public(self):
        print('public() method of C.')

c = C()

#多态
class Animal():                             #定义基类
    def show(self):
        print("I'm an animal.")

class Cat(Animal):                          #派生类
    def show(self):
        print("I'm a cat.")

class Dog(Animal):                          #派生类
    def show(self):
        print("I'm a dog")

class Tiger(Animal):                        #派生类
    def show(self):
        print("I'm a tiger.")

class Test(Animal):                      #派生类,没有覆盖基类的show()方法
    pass
x = [item() for item in (Animal,Cat,Dog,Tiger,Test)]
for item in x:
    item.show()

#接口注入
class Itest():                           #接口
    def injection(self,testClass):
        ''''''

class Test_it(Itest):                    #继承接口
    def injection(self,testObject):      #实现接口方法
        self.object =testObject

    def show(self):                      #普通方法
        print(self.object)

class A_for_itest():                     #测试类
    pass

class B_for_itest():
    pass

t = Test_it()
t.injection(A_for_itest())               #传入不同类型的对象
t.show()
t.injection(B_for_itest())
t.show()

#set注入

class Test_for_set():                   #可实现依赖注入
    def setObject(self,testObject):
        self.object = testObject

    def show(self):
        print(self.object)


t = Test_for_set()
t.setObject(A_for_itest)                    #传入不同类型的对象
t.show()
t.setObject(B_for_itest)
t.show()


#构造注入
class Test_for_construction():
    def __init__(self,testObject):          #通过构造方法实现依赖注入
        self.object = testObject
    def show(self):
        print(self.object)

t1 = Test_for_construction(A_for_itest())
t1.show()
t2 = Test_for_construction(B_for_itest())
t2.show()

#反射
class Animal_for_reflect():                     #定义一个类
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)


class Person_for_reflect(Animal_for_reflect):   #派生类,也可以是一个普通的新类
    pass

a = globals()['Animal_for_reflect']('dog_for_reflect')
a.show()

p = globals()['Person_for_reflect']('zhangsan_for_reflect')
p.show()


#反射的另一种方式
def createObject(testClass, name):
    return testClass(name)

a = createObject(Animal_for_reflect,'cat')
a.show()
b = createObject(Person_for_reflect,'lisi')
b.show()