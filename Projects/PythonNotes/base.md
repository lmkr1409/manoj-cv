- [1. Running Python](#1-running-python)
  - [1.1. Exit Python](#11-exit-python)
- [2. Variables](#2-variables)
    - [2.0.1. Q. What is typing of a language?](#201-q-what-is-typing-of-a-language)
- [3. Conditionals](#3-conditionals)
    - [3.0.1. Python expressions for conditionals](#301-python-expressions-for-conditionals)
    - [3.0.2. ID Function](#302-id-function)
- [4. Data Types](#4-data-types)


# 1. Running Python
1. From command prompt

        python filename.py
2. From Python interpreter
        
        >>> exec(open('filename.py').read())
        
    This can be written as 

        >>> exec(fileObject, global_variable, local_variable)
    Where global_variable and local_variable are optional parameters.

## 1.1. Exit Python

        sys.exit()

# 2. Variables

python is dynamically typed language, variable are assigned automatically.

### 2.0.1. Q. What is typing of a language?


<br/>A.) Typing of a language is 2 parts
> Static/Dynamic Typing is about when type information is acquired.(Either compile time or runtime)

Example:

```Java
String var = "String Value";
```
In Java typing information is quired at compile time. If we assign like below
```java
var = 5;
```
java will raise an error at compile time.

> Strong/Weak Typing is about how strictly types are distinguished.

Example:
In Python
```python
output = 5+"string"
```
will raise a **TypeError** where as in PHP it won't.

So, Python is dynamically strongly typed language


# 3. Conditionals
Key words: **if**, **elif**, **else**
```python
if a<b:
    print("a")
elif a>b:
    print("b")
else:
    print("Both")
```

Conditionals can perform boolean expressions by using **and**, **or**, **not** keywords.

```python
if a<b and b>c:
    print("B is greater than A and C")
```
### 3.0.1. Python expressions for conditionals

```python
expression1 if boolean_expression else expression2
```
Few examples:
```python
>>> 5 if True else 10
5
>>> 5 if 0 else 10
10
>>> a = 100+10 if b else 0
>>> # Here a will be set with 110 if b is true else 0
>>> a = 100 + (10 if b else 0)
>>> # Here a will be set with 110 if b is true else 100
```

### 3.0.2. ID Function

id() function takes an object as a parameter returns the identity of that object.
```python
>>> n = 5 
>>> id(n)
xyz #Some random number
>>> m = n
>>> id(m)
xyz # same random number
>>> n = 6
>>> id(n)
xy #Another random number
>>> id(m)
xyz
```

# 4. Data Types
We can split data types in python to several types
* Numeric Data Types
    * int
    * float
    * complex number
* [Sequence Types](important_topics.html)
    * bytearray
    * bytes
    * str
    * list
    * tuple
* Set Types
    * set
    * frozenset
* Mapping Types
    * dict
    * defaultdict
    * OrderedDict
* boolean