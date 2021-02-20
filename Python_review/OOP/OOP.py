# 类的定义与使用
# 基本语法


class Car(object):  # 定义一个类,派生自object类
    def info(self):  # 定义成员方法
        print('This is a car.')


car = Car()  # 实例对象
car.info()  # 调用对象的成员方法

# isinstance()来测试一个对象是否为某个对象的实例,或者使用内置函数type()来查看对象类型
isinstance(car, Car)
print(type(car))

'''python提供了一个关键字pass,执行的时候什么也不会发生,可以类和函数的定义或选择结构中,表示空语句'''


class Test:
    '''this is a test'''
    pass


Test.__doc__  # 查看类的帮助文档

# %%
# type类
'''type是一个特殊的类,可以看作所有类型(包括object)的基类,
另外python对象都有一个成员__claass__可以查看其所属的类,与内置
函数type()的返回结果一致,所有python类都有一个成员__bases__,返回包含
该类的所有基类的元祖,python类的另一个成员__subclass__()可以返回该
类型的所有子类'''

car.__class__

car.__class__.__class__  # 自定义类型的基类是tyoe

x = 3
x.__class__
x.__class__.__class__  # 整型Int的基类也是type

x = object()
x.__class__
x.__class__.__class__  # object的基类也是type


def f():
    pass


f.__class__  # 查看对象所属类型
type(f)

''.__class__

().__class__
[].__class__
{}.__class__
{}.__class__.__bases__
{}.__class__.__bases__[0].__subclasses__()

# object.__class__.__bases__()[0]

# 退出python 环境,接续程序
# [c for c in ().__class__.__bases_s_[0].__subclasses__()]

# %%
# 定义带装饰器的类

'''与函数一样,定义类时也可以使用装饰器.假设用户创建文件,修改文件,删除文件,查看文件列表等操作都需要先登录系统才行,
每个操作之前都需要确定用户是否已经成功登陆,可以使用python扩展库中的修饰器stateful来实现'''
import state
import os


@state.stateful
class User(object):
    class SignIn(state.State):
        default = True

        @state.behavior
        def signIn(self, userName, userPwd):
            if userName == 'admin' and userPwd == 'admin':
                print('Successfully logged in.')
                # 如果成功登陆就切换至工作状态
                state.switch(self, User.SignedIn)

    class SignedIn(state.State):
        @state.behavior
        def createFile(self):
            with open('test.txt', 'w') as fp:
                fp.write('created')

        @state.behavior
        def modifyFile(self):
            if not os.path.exists('test.txt'):
                return
            with open('test.txt', 'a+') as fp:
                fp.write('ok')

        @state.behavior
        def deleteFile(self):
            if os.path.exists('test.txt'):
                os.remove('test.txt')

        @state.behavior
        def listFile(self):
            for f in os.listdir('.'):
                print(f)


zhang = User()
zhang.signIn('admin', 'admin')
zhang.listFile()
zhang.createFile()
zhang.modifyFile()
# zhang.listFile()

# zhang.deleteFile()

# %%
# 数据成员与成员方法
'''私有成员在类的外部不能直接访问,一般是在类的内部进行访问和操作,或者在类
的外部通过调用对象的公有成员方法来访问,而公有成员是可以公开使用的,既可以在
类的内部进行访问,又可以在外部程序中使用
    如果成员名以两个(或更多)下划线开头但是不以两个或更多下划线结束则表示是私有成员,
否则就不是私有成员,python并没有对私有成员提供严格的访问保护机制,通过一种特殊方式
"对象名__.类名.__xxx"也可以在外部程序中访问私有变量,但这样会破坏类的封装性,不建议
这样做.'''


class A:
    def __init__(self, value1=0, value2=0):  # 构造方法
        self._value1 = value1
        self.__value2 = value2  # 私有成员

    def setValue(self, value1, value2):
        self._value1 = value1
        self.__value2 = value2

    def show(self):
        print(self._value1)
        print(self.__value2)


a = A()
a._value1  # 在类的外部可以直接访问非私有成员
a._A__value2  # 在外部访问对象的私有数据成员

'''从严格意义上讲,这与python的名称绑定机制有关系,在类中以两个或更多下划线开头但不以两个或更多下划线结束的
成员绑定到对象时,都会绑定为"对象名._类名.__成员名类似的形式,除非类名中只包含下划线"'''


class Demo:

    def __init__(self, v):
        self.____value = v


d = Demo(3)
d._Demo____value  # 访问形式被转换


class __:
    def __init__(self, v):
        self.____value = v


dd = __(5)
dd.____value  # 不转换访问形式

'''_xxx:以一个下划线开头,保护成员,只有类对象和子类对象可以访问这些成员,在类的外部一般不建议直接访问,在模块中
使用一个或多个下划线开头的成员不能用 from module import * 导入,除非模块中使用__all__变量明确指明这样的成员
可以被导入
__xxx__: 前后各两条下划线,系统定义的特殊成员
__xxx: 以两个或更多下划线开头但不以两个或更多下划线结束,表示私有成员,一般只有类对象自己能访问,子类对象也不能访问该
成员,但在对象外部可以通过"对象名._类名__xxx这样的特殊方式来访问"
'''

# %%
# 数据成员
''' 数据成员大致上分为两类:属于对象的数据成员和属于类的数据成员,属于对象的数据成员一般在__init__()中定义,当然也可以在其他成员
方法中定义,在定义和在实例方法中访问是以self作为前缀,同一个类的不同对象(实例)的数据成员之间互不影响;
    属于类的数据成员是该类所有对象共享的,不属于任何一个对象,在定义类时这类数据成员一般不在任何一个成员方法的定义中.
    在主程序或类的外部,对象数据成员属于实例(对象),只能通过对象名访问;而类数据成员属于类,可以通过类名或对象名访问'''


class Demo:
    total = 0

    def __new__(cls, *args, **kwargs):  # 该方法在__init__()之前被调用
        if cls.total >= 3:
            raise Exception('最多只能创建3个对象')
        else:
            return object.__new__(cls)

    def __init__(self):
        Demo.total = Demo.total + 1


t1 = Demo()
t2 = Demo()
t3 = Demo()
t4 = Demo()

# %%
# 成员方法,类方法,静态方法,抽象方法
'''方法一般指与特定实例绑定的函数,通过对象调用方法时,对象本身将作为第一个参数自动传递过去,普通函数并不具备这个特点
例如,内置函数sorted()必须要知名要排序的对象,而列表对象的sort()则不需要,默认是对当前列表进行排序'''


class Demo:
    pass


t = Demo()


def test(self, v):
    self.value = v


t.test = test  # 动态的增加普通函数
t.test
t.test(t, 3)  # 需要为self传递参数
print(t.value)

import types

t.test = types.MethodType(test, t)  # 动态增加绑定方法
t.test
t.test(5)  # 不需要为self传递参数
print(t.value)

'''
公有方法,私有方法和抽象方法一般是指属于对象的实例方法,
私有方法的名字以两个或更多下划线开始,
而抽象方法一般定在抽象类中并且要求派生类必须重新实现
公有方法通过对象名直接调用,似有方法不能通过对象名直接调用,只能在其他实例中通过前缀self进行调用或在外部通过特殊形式来调用'''

'''静态方法和类方法都可以通过类名和对象名调用,大不能直接访问属于对象的成员,只能访问属于类的成员'''


class Root:
    __total = 0

    def __init__(self, v):  # 构造方法,特殊方法
        self.__value = v
        Root.__total += 1

    def show(self):
        print('self.__value:', self.__value)
        print('Root.__total:', Root.__total)

    @classmethod  # 修饰器,声明类方法
    def classShowTotal(cls):  # 类方法,一般以cls作为第一个参数的名字
        print(cls.__total)

    @staticmethod  # 修饰器,声明类方法
    def staticShowTotal():  # 静态方法,可以没有参数
        print(Root.__total)


r = Root(3)
r.classShowTotal()  # 通过对象来调用类方法
r.staticShowTotal()  # 通过对象来调用静态方法
rr = Root(5)
Root.classShowTotal()  # 通过类名调用类方法
Root.staticShowTotal()  # 通过类名调用静态方法
# Root.show()  # 试图通过类名直接调用实例方法,报错
Root.show(r)  # 可以通过这种方式来调用方法并访问实例成员

# 抽象方法一般在抽象类中定义,并且在派生类中必须重新实现,否则不允许派生类创建实例
import abc


class Foo(metaclass=abc.ABCMeta):  # 抽象类
    def f1(self):  # 普通实例方法
        print(123)

    def f2(self):
        print(456)  # 普通实例方法

    @abc.abstractmethod  # 抽象方法
    def f3(self):
        raise Exception('You must reimplement thie method')


class Bar(Foo):
    def f3(self):  # 必须重新实现基类中的抽象方法
        print(33333)


b = Bar()
b.f3()

# %%
# 属性
'''属性是一种特殊形式的成员方法,结合了公开数据成员和成员方法的优点,既可以像成员方法那样对值进行必要的检查,
又可以像数据成员一样灵活地访问'''


class Test:
    def __init__(self, val):
        self.__value = val  # 私有数据成员

    @property  # 修饰器,定义属性,提供对私有数据成员的访问
    def value(self):
        return self.__value


t = Test(3)
t.value


# t.value = 5  # 只读属性不允许修改值
# del t.value  # 试图删除对象属性,失败

# 下面代码把属性设置为可读,可修改,而不允许删除

class Test:

    def __init__(self, val):
        self.__value = val

    def __get(self):
        return self.__value

    def __set(self, v):
        self.__value = v

    value = property(__get, __set)  # 可读可写属性,指定对应的读写方法

    def show(self):
        print(self.__value)


print(t.value)  # 允许读取属性值
t = Test(3)
t.value = 5  # 允许修改值
t.value
t.show()


# del t.value   # 试图删除属性,失败

# 也可以把属性设置为可读,可修改,可删除

class Test:
    def __init__(self, val):
        self.__value = val

    def __get(self):
        return self.__value

    def __set(self, v):
        self.__value = v

    def __del(self):  # 删除对象的私有数据成员
        del self.__value

    value = property(__get, __set, __del)  # 可读,可写,可删除的属性

    def show(self):
        print(self.__value)


t = Test(3)
t.show()
t.value = 5
t.value
del t.value
# t.value   # 相应的私有数据成员已删除,访问失败
# t.show()
t.value = 1  # 动态增加属性和对应的私有数据成员
t.show()
t.value

# %%
# 类与对象的动态性,混入机制
'''在python中可以动态地自定义类和对象增加数据成员和成员方法,这也是python动态类型的一种重要体现'''

import types


class Car(object):
    price = 100000  # 属于类的数据成员

    def __init__(self, c):
        self.color = c


car1 = Car('red')  # 实例化对象
print(car1.color, Car.price)  # 访问对象和类的数据成员
Car.price = 110000  # 修改类属性
Car.name = 'QQ'  # 动态增加类属性
car1.color = 'yellow'
car1.year = 10  # 增加成员属性
print(car1.color, Car.price, Car.name)


def setSpeed(self, s):
    self.speed = s


car1.setSpeed = types.MethodType(setSpeed, car1)  # 动态为对象增加成员方法
car1.setSpeed(50)
print(car1.speed)

'''python类型的动态性使得我们可以动态为自定义类及其对象增加新的属性和行为,俗称混入(mix)机制,'''
import types


class Person(object):
    def __init__(self, name):
        assert isinstance(name, str), 'name must be string'
        self.name = name

    #
    # def sing(self):
    #     print(self.name + ' can sing')

    # def walk(self):
    #     print(self.name + ' can walk')

    def eat(self):
        print(self.name + ' can eat')


zhang = Person('zhang')


def sing(self):
    print(self.name + ' can sing')


def walk(self):
    print(self.name + ' can walk')


zhang.sing = types.MethodType(sing, zhang)  # 动态增加一个新行为
zhang.sing()

zhang.walk = types.MethodType(walk, zhang)  # 动态增加一个新行为
zhang.walk()

# del zhang.walk
# zhang.walk()


# %%
# 继承,多态,依赖注入

'''设计一个新类时,如果可以继承一个已有的设计良好的类然后进行二次开发,可以大幅度减少开发工作量,
并且可以很大程度地保证质量.在继承关系中,已有的,设计好的类称为父类或基类,新设计的类称为子类或派生类.
派生类可以继承负累的共有成员,但是不能继承其私有成员.如果需要在派生类中调用基类的方法,可以使用内置函数super()
或通过基类名.方法名()的方式来实现这一目的'''


# 基类必须继承与object,否则在派生类中将无法使用super()函数
class Person(object):
    def __init__(self, name='', age=20, sex='man'):
        # 通过调用方法进行初始化,这样可以对参数进行更好的控制
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

        # 用私有数据成员,进行初始化
        # self.__name = name
        # self.__age = age
        # self.__sex = sex

    def setName(self, name):
        if not isinstance(name, str):
            raise Exception('name must be a string')
        self.__name = name

    def setAge(self, age):
        if type(age) != int:
            raise Exception('Age must be an interger')
        self.__age = age

    def setSex(self, sex):
        if sex not in ('man', 'woman'):
            raise Exception('sex must be man or woman')
        self.__sex = sex

    def show(self):
        print(self.__name, self.__age, self.__sex)


# 派生类
class Teacher(Person):
    def __init__(self, name='', age=30, sex='man', department='Computer'):
        # 调用基类构造方法初始化基类的私有数据成员
        super(Teacher, self).__init__(name, age, sex)
        # 也可以这样初始化基类的私有数据成员
        # Person.__init__(self, name, age, sex)
        # 初始化派生类的数据成员
        self.setDepartment(department)

    def setDepartment(self, department):
        if type(department) != str:
            raise Exception('department must be a string')
        self.__department = department

    def show(self):
        super(Teacher, self).show()
        print(self.__department)


if __name__ == '__main__':
    # 创建基类对象
    zhangsan = Person('zhang san', 19, 'man')
    zhangsan.show()

    # 创建派生类对象
    lisi = Teacher('li si', 32, 'woman', 'Math')
    lisi.show()

    # 调用继承的方法修改年龄
    # lisi.setAge(39)
    # lisi.show()

'''python支持多继承,如果父类中有相同的方法名,而在子类中使用时没有指定父类名,则python解释器将从右向左
按顺序进行搜索,使用第一个匹配的成员'''


class A():
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private() method of A')

    def public(self):
        print('public() method of A')

    def __test(self):
        print('__test() method of A')


class B(A):
    def __private(self):
        print('__private() method of B')

    def public(self):
        print('public() method of B')


b = B()
# b._B__test()  # 派生类没有继承基类中的私有成员方法
b._A__test()  # 通过特殊方法可以访问基类中的私有成员方法
b._A__private()  # 没有严格意义的私有成员


class C(A):  # 注意,C类有构造方法
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private() method of C')

    def public(self):
        print('public() of method of C')


c = C()

# %%
# 多态
'''多态(polymorphism)是指基类的同一个方法在不同派生类对象中具有不同的表现和行为.
派生类继承了基类的行为和属性之后,还会增加某些特定的行为,同时还会对继承来的某些行为进行一定的改变,
这都是多态的表现形式'''


class Animal(object):
    def show(self):
        print("I'm an animal")


class Cat(Animal):  # 派生类,覆盖了基类的shou()方法
    def show(self):
        print('I am a cat')


class Dog(Animal):  # 派生类
    def show(self):
        print("I am a dog.")


class Tiger(Animal):  # 派生类
    def show(self):
        print('I am a Tiger')


class Test(Animal):  # 派生类,没有覆盖基类的show()方法
    pass


x = [item() for item in (Animal, Cat, Dog, Tiger, Test)]

for item in x:
    item.show()

# %%
# 依赖注入技术的不同实现方法
'''依赖注入又称为控制反转,主要用来实现不同模块或类之间的解耦'''
# 1.接口注入
'''首先定义一个接口类,然后再继承了该接口的类中实现特定的接口方法,
而在接口方法中根据传入参数的不同作出不同的行为'''


class ITest:
    def injection(self, testClass):  # 接口
        ''''''


class Test(ITest):  # 继承接口
    def injection(self, testObject):  # 实现接口方法
        self.object = testObject

    def show(self):
        print(self.object)


class A:  # 类A和B是测试用的
    pass


class B:
    pass


t = Test()
t.injection(A())  # 传入不同类型的对象
t.show()
t.injection(B())
t.show()

# 2.Set注入
'''通过类本身提供的一个方法注入不同类型的对象来设置自身对象和其他对象的依赖关系'''


class Test:
    def setObject(self, testObject):  # 可实现依赖注入
        self.object = testObject

    def show(self):
        print(self.object)


class A:
    pass


class B:
    pass


t = Test()
t.setObject(A())  # 传入不同类型的对象
t.show()
t.setObject(B())
t.show()

# 3.构造注入
'''通过创建类的实例方法时为构造方法传入不同类型的对象实现'''


class Test:
    def __init__(self, testObject):  # 通过构造方法实现依赖注入
        self.object = testObject

    def show(self):
        print(self.object)


class A:
    pass


class B:
    pass


t = Test(A())
t.show()
t = Test(B())
t.show()

# 4. 反射
'''通过反射技术可以根据传入信息(例如类的名字)的不同来创建不同类型的对象,
从而实现多态和依赖注入'''


class Animal:  # 定义一个类
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Person(Animal):  # 继承Animal类,也可以是一个普通的新类
    pass


a = globals()['Animal']('dog')  # 简单形式的反射
a.setName('li')
a.show()

p = globals()['Person']('zhangsan')  # 根据类的名字不同来创建不同的对象
p.show()


# 下面演示反射的另一种形式
class Animal:
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Person(Animal):  # 继承Animal类,也可以是一个普通的新类
    pass


def createObject(testClass, name):
    return testClass(name)


a = createObject(Animal, 'dog')
a.show()

p = createObject(Person, 'zahngsan')
p.show()

# %%
# 构造方法和运算符重载
'''python类中有大量的特殊方法,其中比较常见的是构造方法和析构方法.python中类的构造方法是__init__(),用来为数据成员设置
初始值或仅向其他必要的初始化工作,在实例化对象时被自动调用和执行,如果用户没有设计构造方法,python会提供一个默认的构造方法用来进行
必要的初始化工作.python中类的析构方法时__del__(),一般用来释放对象占用的资源,在python删除对象和收回对象空间时被自动调用和执行.
如果用户没有编写析构方法,python将会提供一个默认的析构方法进行必要的清理工作
    在python中,除了构造方法和析构方法之外,还有大量的特殊方法支持更多的功能.例如,运算符重载就是通过在类中重写特殊方法实现的.
在自定义类时如果重写某个特殊方法即可支持对应的晕撒u农夫或内置函数.'''


class test:
    def __new__(cls, *args, **kwargs):  # 类的静态方法,用于确定是否创建对象
        pass

    def __init__(self):  # 构造方法,创建对象时自动调用
        pass

    def __add__(self, other):  # '+'
        pass

    def __sub__(self, other):  # '-'
        pass

    def __mul__(self, other):  # '*'
        pass

    def __truediv__(self, other):  # '/'
        pass

    def __floordiv__(self, other):  # '//'
        pass

    def __mod__(self, other):  # '%'
        pass

    def __pow__(self, power, modulo=None):  # '%%'
        pass

    def __eq__(self, other):  # '=='
        pass

    def __ne__(self, other):  # '!='
        pass

    def __lt__(self, other):  # '<'
        pass

    def __le__(self, other):  # '<='
        pass

    def __gt__(self, other):  # '>'
        pass

    def __ge__(self, other):  # '>='
        pass

    def __lshift__(self, other):  # <<
        pass

    def __rlshift__(self, other):  # >>
        pass

    def __and__(self, other):  # &
        pass

    def __or__(self, other):  # |
        pass

    def __invert__(self):  # ~
        pass

    def __xor__(self, other):  # ^
        pass

    def __iadd__(self, other):  # += 很多其他运算符也有与之对应的符合赋值运算符
        pass

    def __isub__(self, other):  # -=
        pass

    def __pos__(self):  # 一元运算符+,正号
        pass

    def __neg__(self):  # 一元运算符-,负号
        pass

    def __contains__(self, item):  # 与成员测试符in对应
        pass

    def __radd__(self, other):  # 反射加法,减法,一般与普通加减法具有相同的功能,但操作数的位置或顺序相反,很多其他运算符
        # 也有与之对应的反射运算符
        pass

    def __rsub__(self, other):
        pass

    def __abs__(self):  # 与内置函数abs()对应
        pass

    def __bool__(self):  # 与内置函数bool()对应,要求该方法必须返回True,或False
        pass

    def __bytes__(self):  # 与内置函数bytes()对应,
        pass

    def __complex__(self):  # 与内置函数complex()对应,要求该方法必须返回实数
        pass

    def __dir__(self):  # 与内置函数dir()对应
        pass

    def __divmod__(self, other):  # 与内置函数divmod()对应
        pass

    def __float__(self):  # 与内置函数float()对应,要求该方法必须返回实数
        pass

    def __hash__(self):  # 与内置函数hash()对应,
        pass

    def __int__(self):  # 与内置函数int()对应,要求该方法必须返回整数
        pass

    def __len__(self):  # 与内置函数len()对应
        pass

    def __next__(self):  # 与内置函数next()对应
        pass

    def __reduce__(self):  # 提供对reduce()函数得到支持
        pass


'''reduce() 函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）
中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 
个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。'''


# reduce(function, iterable[, initializer])
# function -- 函数，有两个参数
# iterable -- 可迭代对象
# initializer -- 可选，初始参数

def add(x, y):  # 两数相加
    return x + y


# 在python3中,reduce被移至functools模块中
from functools import reduce

ls = reduce(add, [1, 2, 3, 4, 5])
print(ls)


class Test2:
    def __reversed__(self):  # 与内置函数reversed()对应
        pass

    def __round__(self, n=None):  # 与内置函数round()对应
        pass

    def __str__(self):  # 与内置函数str()对应,要求该方法必须返回str类型的数据
        pass

    def __repr__(self):  # 打印,转换,要求该方法必须返回str类型数据
        pass

    def __getitem__(self, item):  # 按照索引获取值
        pass

    def __setitem__(self, key, value):  # 按照索引赋值
        pass

    def __delattr__(self, item):  # 删除对象的指定属性
        pass

    def __getattr__(self, item):  # 获取对象指定属性的值,对应成员访问运算符"."
        pass

    def __getattribute__(self, item):
        """获取对象指定属性的值,如果同时定义了该方法与__getattr__(),那么后者不会被调用,除非在
        __getattribute__()中显式调用后者,或者抛出AttributeError异常"""
        pass

    def __setattr__(self, key, value):  # 设置对象制定属性的值
        pass

    def __call__(self, *args, **kwargs):    # 包含该特殊方法的类的实例可以像函数一样调用
        pass


    '''定义了这3个特殊方法中任何一个的类称为描述符,描述符对象一般作为其他类的属性来使用
    这三个方法分别用在获取属性,修改属性值或删除属性时被调用'''
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


test1 = Test2()
# print(Test2.__bases__)  # 该类的基类
# print(Test2.__class__)
print(Test2.__class__)  # 返回对象所属的类
print(Test2.__dict__)   # 对象所包含的属性与值的字典
print(Test2.__subclasses__())   # 返回该类的所有子类
