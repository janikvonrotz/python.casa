#!/usr/bin/env python3
a = 3

def f():
    a = 4
    print('locals() in f:', locals())
    # Ausgabe f: {'a': 4}
    return a
  
class C():
    def __init__(self, a, b):
        self.a = a
        self.b = b
      
    def m(self):
        return self.a + self.b
  
result = f()
print('vars(f):', vars(f))
# Ausgabe: {}

obj = C(1, 2)
print('vars(obj):', vars(obj))
# Ausgabe: {'a': 1, 'b': 2}

print('globals():', globals())
# Ausgabe: {'__name__': '__main__', 
#           '__doc__': None, 
#           '__package__': None, 
#           '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x103b89080>, 
#           '__spec__': None, 
#           '__annotations__': {}, 
#           '__builtins__': <module 'builtins' (built-in)>, 
#           '__file__': './local-global.py', 
#           '__cached__': None, 
#           'a': 3, 
#           'f': <function f at 0x103b201e0>, 
#           'C': <class '__main__.C'>, 
#           'result': 4, 
#           'obj': <__main__.C object at 0x103c25f28>}




