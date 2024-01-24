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

list1 = [1,2,3,'4',[5]]
list2 = list()

print(list1[-1]) #last element
list1[0] = 'one'
print(list1[0])
print(list1[0:3]) #elements - index 0,1,2 -> 3 - not inclued 
print(list1[::2])
print(2 in list1)
list2.append(10)
list2.append(20)
print(list2)
list3 = list1 + list2
print(list3, list1)
list1.extend(list2)
print(list1)
x, y = list2
print(x, y)
_, y = list2
print(_, y)
list4 = [_ for _ in range(100)]
print(len(list4))

tuple1 = (1,2,3)
try:
    tuple1[0] = tuple1[0] * 10
except:
    print('Cannot change a tuple value.')

def sum_and_product(x: int, y: int) -> int:
    return x + y, x * y #returns as a tuple
s, p = sum_and_product(3, 4)

print(sum_and_product(1,2))
print(s, p)

a1, b1 = 1, 2
a1, b1 = b1, a1
print(a1, b1)

grades_dict = {'joel': 80, 'tim': 90}
print(grades_dict['joel'], 'joel' in grades_dict)
print(grades_dict.get('sdfsdfsdf'))
grades_dict['kate'] = 99
print(grades_dict['kate'])
print(grades_dict.keys(), grades_dict.values(), grades_dict.items())
grades_dict[('hashalbe', 'key')] = 100
grades_dict['hashablekey2'] = 100
print(grades_dict)

words = ['aaaa', 'bbbb', 'cccc', 'aaaa', 'aaaa', 'cccc']
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
print(words_count)

from collections import defaultdict

word_counts2 = defaultdict(int) #atribui 0 a valor das novas chaves - int()
for word in words:
    word_counts2[word] += 1 #incrementa o novo valor da chave criada como 0
print(word_counts2.items())

from collections import Counter

word_counts3 = Counter(words)
print(word_counts3)

for word, count in word_counts3.most_common(1): # top 1 com maior contagem
    print(word, count)

set1 = {1,2,3}
empty_set = set() #{} é um dict vazio
empty_set.add(1)
print(set1, empty_set)
words_set = set(words)
print('aaaa' in words_set) #mt mais rápido do que procurar em uma lista