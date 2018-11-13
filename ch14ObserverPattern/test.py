class ObjectCreator():
    pass


def echo(o):
    print(o)

def i(o):
    print(o)


def choose_class(name):
    if name=="foo":
        class Foo():
            pass
        return Foo
    else:
        class Bar():
            pass
        return Bar


class MyShinyClass():
    pass



my_object=ObjectCreator()
echo(my_object)
echo(ObjectCreator)
echo(hasattr(ObjectCreator,"new_attribute"))
ObjectCreator.new_attribute="foo"
echo(hasattr(ObjectCreator,"new_attribute"))

ObjectCreatorMirror=ObjectCreator
echo(ObjectCreatorMirror)
echo(ObjectCreatorMirror())

Myclass=choose_class("foo")
echo(Myclass)
echo(Myclass())
echo(type(1))
echo(type("1"))
echo(type(ObjectCreator))
echo(type(ObjectCreator()))
MyShinyClass=type("MyShinyClass",(),{})
echo(MyShinyClass)
echo(MyShinyClass())
Foo=type('Foo',(),{'bar':True})
i(Foo)
i(Foo.bar)
f=Foo()
i(f.bar)

class Foochild(Foo):
    pass
i(Foochild)
i(Foochild.bar)

def echo_bar(self):
    print("FooXXXXX.bar ::::"+str(self.bar))

Foochild=type("Foolchild",(Foo,),{"echo_bar":echo_bar})
i(hasattr(Foo,'echo_bar'))
i(hasattr(Foochild,'echo_bar'))
my_foo=Foochild()
my_foo.echo_bar()

# MyClass=MetaClass()

age=35
i(age.__class__)
i(age.__class__.__class__)
name="bob"
i(name.__class__)
i(name.__class__.__class__)
def foo(): pass
i(foo.__class__)
i(foo.__class__.__class__)

class Bar(): pass

bar=Bar()
i(bar.__class__)
i(bar.__class__.__class__)

def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attrs)



class Fooo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    __metaclass__ = UpperAttrMetaClass
    bar = 'bip'

i(hasattr(Fooo, 'bar'))
# 输出: False
i(hasattr(Fooo, 'BAR'))
# 输出:True

f = Fooo()
i(f.BAR)
# 输出:'bip'