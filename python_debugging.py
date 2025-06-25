'''
1.
 def greet(name)
 print("Hello, " + name)
'''
def greet(name):
    print("Hello, " + name)

greet("Jeevitha")


'''
2. ```python
if x = 10:
 print(x)
'''
x = 10 
if x == 10:  
    print(x)

'''
3.
list = [1, 2, 3
print(list)
'''
list = [1, 2, 3]
print(list)


'''
4. ```python
print "Hello World"
'''

print("Hello World")



'''
5.
for i in range(5)
print(i)
'''
for i in range(5):
    print(i)

'''
6. ```python
def add(a, b):
return a + b
'''

def add(a, b):
    return a + b

'''7.
name = input('Enter name: ')
print('Hello, ' + name)'''

name = input('Enter name: ')
print('Hello, ' + name)

'''
8. ```python
my_dict = {'a': 1, 'b': 2, 'c': 3
print(my_dict['b'])
'''
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['b'])

'''9.
a = 5
b = '5'
print(a + b)
10. ```python
def func(x, y=2, z):
 return x + y + z
'''
a = 5
b = '5'
print(a + int(b))  


'''10. ```python
def func(x, y=2, z):
 return x + y + z'''
def func(x, z, y=2):
    return x + y + z

'''11.
def is_even(n):
return n % 2 == 1'''
def is_even(n):
    return n % 2 == 0

'''
12. ```python
def factorial(n):
 result = 1
 for i in range(n):
 result *= i
 return result
'''

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

'''
13.
def reverse_list(lst):
return lst.sort()
'''

def reverse_list(lst):
    return list(reversed(lst))

'''14. ```python
def find_max(numbers):
 max = 0
 for n in numbers:
 if n > max:
 max = n
 return max'''

def find_max(numbers):
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

'''15.
def average(numbers):
return sum(numbers) / len(numbers) if numbers != None else 0'''
def average(numbers):
    return sum(numbers) / len(numbers) if numbers is not None else 0

'''
16. ```python
for i in range(10):
 if i == 5:
 break
 else:
 continue
 print(i)
'''
for i in range(10):
    if i == 5:
        break
    print(i)

'''
17.
a = [1, 2, 3]
b = a
b.append(4)
print(a) # Expect [1, 2, 3]
'''
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # Output: [1, 2, 3, 4]

'''
18. ```python
x = 5
def change():
 x = 10
change()
print(x)
'''
x = 5
def change():
    global x
    x = 10
change()
print(x)

'''
19.
nums = [10, 20, 30, 40]
print(nums.index(100))
'''
nums = [10, 20, 30, 40]
print(nums.index(100) if 100 in nums else "Not found")

'''
20. ```python
a = 0.1 + 0.2
print(a == 0.3)
'''
import math
a = 0.1 + 0.2
print(math.isclose(a, 0.3))

'''
21.
print(1 / 0)

'''
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

'''
22. ```python
try:
 my_list[5]
except:
 print('An error occurred')
'''
my_list = [1, 2, 3]
try:
    my_list[5]
except:
    print('An error occurred')

'''
23.
def divide(a, b):
try:
return a / b
except ZeroDivisionError:
return "Can't divide by zero"
finally:
return "Done"
'''

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"

print(divide(4, 2))

'''
24. ```python
d = {'x': 1, 'y': 2}
print(d['z'])
'''
d = {'x': 1, 'y': 2}
print(d.get('z', 'Key not found'))

'''
25.
f = open('file.txt')
print(f.read())

'''
try:
    f = open('file.txt')
    print(f.read())
except FileNotFoundError:
    print("File not found")

'''
26. ```python
import math
print(math.sqrt(-1))
'''
import cmath
print(cmath.sqrt(-1))

'''
27.
a = [1, 2, 3]
print(a[3])
'''

a = [1, 2, 3]
print(a[3] if len(a) > 3 else "Index out of range")

'''
28. ```python
s = 'hello'
print(int(s))
'''
s = 'hello'
try:
    print(int(s))
except ValueError:
    print("Cannot convert to int")

'''
29.
from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d %h:%m:%s'))
'''
from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

'''
30. ```python
int_list = list(map(int, ['1', '2', 'three', '4']))
'''
values = ['1', '2', 'three', '4']
int_list = []
for v in values:
    try:
        int_list.append(int(v))
    except ValueError:
        continue
print(int_list)

'''
31.
def increment(n):
n += 1
increment(5)
print(n)
'''
def increment(n):
    n += 1
    print(n)

increment(5)

'''
32. ```python
counter = 0
def increase():
 global counter
 counter += 1
increase()
print(counter)
'''
counter = 0
def increase():
    global counter
    counter += 1

increase()
print(counter)

'''
33.
def append_item(item, lst=[]):
lst.append(item)
return lst
'''

def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

'''
34. ```python
def greet(name, greeting='Hello'):
 return greeting + name
print(greet('John', greeting='Hi', 'Mr.'))
'''
def greet(name, greeting='Hello', title=''):
    return greeting + ' ' + title + name

print(greet('John', greeting='Hi', title='Mr. '))


'''
35.
x = 10
def outer():
x = 20
def inner():
print(x)
inner()
outer()
'''
x = 10
def outer():
    x = 20
    def inner():
        print(x)
    inner()
outer()

'''
36. ```python
def modify_list(lst):
 lst = lst + [1]
my_list = [0]
modify_list(my_list)
print(my_list)
'''
def modify_list(lst):
    lst.append(1)
my_list = [0]
modify_list(my_list)
print(my_list)

'''
37.
def test():
return
print('unreachable')
'''
def test():
    return

print('unreachable')

'''
38. ```python
a = [1, 2, 3]
for i in a:
 a.remove(i)
print(a)
'''
a = [1, 2, 3]
for i in a[:]:
    a.remove(i)
print(a)

'''
39.
def multiply(a, b):
return a * b
print(multiply(2))
'''
def multiply(a, b):
    return a * b

print(multiply(2, 3)) 


'''
40. ```python
def square(x):
 print(x ** 2)
result = square(4)
print(result)
'''
def square(x):
    return x ** 2

result = square(4)
print(result)

'''
41.
my_set = set([1, 2, 3])
print(my_set[0])
'''
my_set = set([1, 2, 3])
print(list(my_set)[0])

'''
42. ```python
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('c', 'No key'))
'''
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('c', 'No key'))

'''
43.
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
print(nums[i + 1])
'''
nums = [1, 2, 3, 4, 5]
for i in range(len(nums) - 1):
    print(nums[i + 1])

'''
44. ```python
i = 0
while i < 5:
 print(i)
'''
i = 0
while i < 5:
    print(i)
    i += 1

'''
45.
my_tuple = (1)
print(type(my_tuple))
'''
my_tuple = (1,)
print(type(my_tuple))

'''
46. ```python
def merge_dicts(d1, d2):
 return d1.update(d2)
'''
def merge_dicts(d1, d2):
    d1.update(d2)
    return d1

'''
47.
for i in range(3):
print(i)
else:
break
'''
for i in range(3):
    print(i)
    if i == 1:
        break

'''
48. ```python
items = ['apple', 'banana', 'cherry']
for i in range(len(items)):
 print(items[i + 1])
'''
items = ['apple', 'banana', 'cherry']
for i in range(len(items) - 1):
    print(items[i + 1])

'''
49.
a = [1, 2, 3]
print(a.pop(3))
'''

a = [1, 2, 3]
print(a.pop(3) if len(a) > 3 else "Index out of range")

'''
50. ```python
def foo():
 try:
 return 1
 finally:
 return 2
print(foo())
'''

def foo():
    try:
        return 1
    finally:
        print("Cleaning up")

print(foo())



