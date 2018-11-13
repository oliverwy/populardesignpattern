import inspect
import re

def vName(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)

class Meta(type):
    pass

class Complex(metaclass=Meta):
    pass

class Complex2(Meta):
    pass

def i(o):
    # print(vName(o))
    print(o)

i(type(Complex))
i(Complex)
i(type(Complex2))
i(Complex2)

class Funky:
    def __call__(self):
        i("Look at me ,I work like a function!")
f=Funky()
f()

class Foobar:
    __slots__ = "A","B","C","D"

foon=Foobar()
foon.A=1
i(foon.A)
#

class Magic:
    @property
    def __repr__(self):
        def inner():
            return "It Works!"
        return inner

i(repr(Magic()))
i(repr(Magic))


class Class(metaclass=Meta):
    a = 1
    b = 2
    c=3
