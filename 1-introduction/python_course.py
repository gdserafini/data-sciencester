import sys
import matplotlib.pyplot as plt
from typing import Any

print('Hello world!')
print(f'Pyhton3 version: {sys.version}')

plt.plot()

def func_with_doc(param: Any) -> Any:
    """This amazing functions returns the passed param :)"""
    return param

print(func_with_doc(1))

#default param
def first_class_func(func = lambda x: x):
    return func(1)

func = func_with_doc
print(first_class_func(func))
print(first_class_func(lambda x: x + 1)) #passa uma função def f(x): return x+1
double = lambda x: x * 2 #não recomendado 

x = 1
def addone(num):
    num += 1
addone(x)
print(x)

string_ex = '\t'
string_ex_r = r'\t'
print(len(string_ex), " ", len(string_ex_r))
print(
    """
    Multi 
Line 
        String
    """
)
print(f'f-string: {1}, {2}, {3}')

#try:
#    print(0/0)
#except Exception as ex:
#    raise ex