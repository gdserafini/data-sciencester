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