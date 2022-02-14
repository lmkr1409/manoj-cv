
A sequence data type is the data type that supports the membership operator *in*, the size function *len()*, slices *[]* and iterable.

Python provides 5 built-n sequence types
* bytearray
* bytes
* str
* list
* tuple

# Common across all sequence types

## Slicing
Examples are using list, but applicable for all sequence types
* Slicing is a technique to extract part of the sequence using indexes. Big brackets [] are used for slicing the sequence
* Sequence starts with 0
* when using slicing endIdx is excluded. 
    * Ex: li[start: end] -> start: included, end: excluded

Consider below list 

        #x[-7]  x[-6]   x[-5]   x[-4]   x[-3]   x[-2]   x[-1]
    x = [1,     2,      3,      4,      5,      6,      7]
        #x[0]  x[1]    x[2]    x[3]    x[4]    x[5]    x[6]

### Syntax
```python
>>> x[start:end:step]
```
* start -> start index(inclusive)
* end -> end_index (excludes)
* step -> what is next index to look at

Examples:
```python
>>> x = [1,2,3,4,5,6,7]
>>> # Single idx slice
>>> x[0]
1
>>> x[-7]
1
```
When end index is not provided, slicing will run till last values of the list. And when start is provided then slice function assumes 0 as start
```python
>>> x[1:]
[2, 3, 4, 5, 6, 7]
>>> x[-2:]
[6, 7]
>>> x[:4]
[1, 2, 3, 4]
>>> x[:-3]
[1, 2, 3, 4]
>>> 
```
When both indexes provided, start is inclusive and end is exclusive
```python
>>> x[2:5] # idx 5 is excluded, so there won't be 6 in output
[3, 4, 5]
>>> x[-3:6]
[5, 6]
>>> x[-5:6]
[3, 4, 5, 6]
>>> x[-3:-5]
[]
>>> x[-5:-3]
[3, 4]
>>> x[3:-3]
[4]
```
With Step 
```python 
>>> x[1:6:1] # step =1, is default
[2, 3, 4, 5, 6]
>>> x[1:6:2] # step =2, skips every second element
[2, 4, 6]
>>> x[1:6:3] # step = 3, skips 2 elements every time 
[2, 5]
>>> x[1:6:4]
[2, 6]
>>> x[1:6:5]
[2]
>>> x[1:6:6]
[2]
>>> x[1:6:100]
[2]
```
Negative step - will iterate the list in reverse order. So, if the start is less than the end then output will be empty.
```python
>>> x[1:6:-1]
[]
>>> x[1::-1]
[2, 1]
>>> x[1:0:-1]
[2]
>>> x[7::-1]
[7, 6, 5, 4, 3, 2, 1]
>>> x[7:0:-1]
[7, 6, 5, 4, 3, 2]
>>> x[7:-7:-1]
[7, 6, 5, 4, 3, 2]
>>> x[7:-8:-1]
[7, 6, 5, 4, 3, 2, 1]
>>> x[7:-8:-2]
[7, 5, 3, 1]
>>>
```

# Lists - Mutable

* In Python a list is an ***ordered sequence*** of zero or more object references.
* Lists are **Mutable** objects.

### Unpacking and starred unpacking of a list:
```python
>>> a,b = [1,2]
>>> a
1
>>> b
2
>>> a, *b, c = [1,2,3,4,5,6]
>>> a
1
>>> b
[2, 3, 4, 5]
>>> c
6
>>> *a, b = [1,2,3,4,5,6]
>>> a
[1, 2, 3, 4, 5]
>>> b
6
>>> 
```

### Methods on lists:
Let **li** be the list object

| method | description|
| -------------------- | -- |
| li.append(x) | append item x to the list li|
| li.count(x) | count number of occurrences of item x in the list li|
| extend(m) <br/> or <br/> li +=li_b | append all items of iterable li_b to the list li|
| li.insert(i,x) | insert item x at position i |
| li.index(x, start, end) | Returns the first occurance of x, if x not found in the list raises **ValueError** |
| li.pop() | returns and removes last (or) right most element |
| li.pop(i) | returns and removes the item at index position int i |
| li.remove(x) | removes the first occurance of item x. If x not found in the list li then **ValueError** will be raised. | 
| li.reverse() | reverses the list | 
| li.sort() | sorts the list |
|

### List Comprehension
A list comprehension is an expression and a loop with an optional condition enclosed in brackets where the loop is used to generate items for the list and where the condition can filter out unwanted items.
```python
>>> [item for item in iterable]
>>> [expression for item in iterable]
>>> [expression for item in iterable if condition]
```

# Tuples - Immutable
A tuple is an ordered sequence of zero or more objects references.
* Same unpacking technique can be used to tuples which we used in lists

### Methods on tuples
Since tuples are immutable there are no methods which does the modification to the sequence.
| Method | Description |
| -- | -- |
| t.count(x) | returns the number of times object x appeared in the tuple t | 
| t.index(x) | index of first occurance of item x in the tuple <br/> **ValueError**: if x not found in tuple t |
|

> Tuples can be used with operators
* \+ concatenation
* \* replication
* [] slice

Note: 
* The += and *= assignment operators can be used with tuple overthought tuples are immutable. 
* Python will create new tuple and change the reference of the object to new tuple
* Tuples can be compared using the standard comparison operators
    * <, <=, ==, !=, >=, >
    * comparison will be applied item by item (and recursively for the nested items)

# Named Tuples
A named tuple behaves just like a plain tuple and has the same performance characteristics. What it adds is the ability to refer to items in the tuple by name as well by index position.
<br/> And this allows us to create aggregates of data items.

```python
>>> from collections import namedtuple
```
named tuple takes in 2 arguments.
1. Custome tuple datatype we want to create
2. A string of space separated names.One for each item that our custome tuple will take.

```python
>>> saleObj = namedtuple("sale", "pid cid quantity")
>>> s = saleObj(1,2,3)
>>> s
sale(pid=1, cid=2, quantity=3)
>>> s[0]
1
>>> s.pid
1
>>> s.cid
2
>>> 
```
For nested namedtuple
```python
>>> afObj = namedtuple("Aircraft", "manufacturer model seating")
>>> stObj = namedtuple("seating", "minimum maximum")
>>> a1 = afObj("Airbus", "A320", stObj(100,200))
>>> a1.seating.minimum
100
>>>
```
### String formatting for namedtuple 
In general string formatting is like below
```python
>>> "{} {}".format(a1.manufacturer, a1.model)
'Airbus A320'
>>>
```
In namedtuple we can use **_asdict()** private method for string formatting.
```python
>>> "{manufacturer} {model}".format(**a1._asdict())
'Airbus A320'
>>> 
```