# What is PyQCheck?

PyQCheck is a Quick Check-like testing framework based on the idea of Haskell Quick Check.

- This framework is for random data testing.
- The function's interface was referred from [macchiato.js](http://voqn.github.com/macchiato/). (from the top page...)

# Which python version does this support? 

This framework worked on python version 2.7.3

# How to Install

```
python setup.py install
```

# How to Use PyQCheck
## Writing test

- At method chain

``` python
from pyqcheck.pyqcheck import PyQCheck, Arbitrary

def eq(x,y):
  return x * y == y * x and x + y == y + x

PyQCheck(verbose=True).add(
  Arbitrary('boolean', 'boolean').property(
    '!(x || y) == !x && !y', lambda x, y: (not(x or y)) == ((not x) and (not y))
  )
).add(
  Arbitrary('integer', 'integer').property(
    'x * y == y * x and x + y == y + x', eq
  )
).run(10).result() # run(10) is test count == 10
```

- At decorator

``` python
from pyqcheck.pyqcheck import PyQCheck, Arbitrary

@set_arbitrary('boolean', 'boolean')
def de_morgan(x, y):
  '''
  !(x || y) == !x && !y', lambda x, y: (not(x or y)) == ((not x) and (not y))
  '''
  return (not(x or y)) == ((not x) and (not y))

@set_arbitrary('integer', 'integer')
def eq(x, y):
  '''
  x * y == y * x and x + y == y + x
  '''
  return x * y == y * x and x + y == y + x

PyQCheck(verbose=True).run(10).result() # run(10) is test count == 10
```

## Test Result.

```
----- PyQCheck test results... -----
label: !(x || y) == !x && !y
success: 10   
failure: 0
verbose:
  ☀  <lambda>(True, True)
  ☀  <lambda>(False, False)
  ☀  <lambda>(False, True)
  ☀  <lambda>(True, True)
  ☀  <lambda>(True, True)
  ☀  <lambda>(True, True)
  ☀  <lambda>(True, True)
  ☀  <lambda>(True, False)
  ☀  <lambda>(False, True)
  ☀  <lambda>(True, False)
-----
label: x * y == y * x and x + y == y + x
success: 10
failure: 0
verbose: 
  ☀  eq(5619883977492185900, 8098677974428651270)
  ☀  eq(1083625604502060169, 8458294345657310737)
  ☀  eq(4669876018772361359, 6247727992957273395)
  ☀  eq(8339760176857203915, 8345011171974202548)
  ☀  eq(7278259878279970866, 4100741748945006135)
  ☀  eq(4817262410454816318, 3084576882465980476)
  ☀  eq(2635121478675656588, 7568822804535567953)
  ☀  eq(6708571901087888356, 1255734967659271542)
  ☀  eq(2208040650061775673, 7460005457506446202)
  ☀  eq(5032528890931210411, 2911935080322536883)
-----
```

# Supports arbitrary data type.

- PyQString ('string')
- PyQInteger ('integer')
- PyQNumber ('number')
- PyQHiragana ('hiragana')
- PyQKatakana ('katakana')
- PyQMomoclo ('momoclo')

# Setting arbitrary limit.

``` python
from pyqcheck.pyqcheck import PyQCheck, Arbitrary

PyQCheck().add(
  Arbitrary(
    ('integer', dict(min=10, max=100)), # range of 10 - 100
    ('integer', dict(min=30)), # range of 30 - max of default
  ).property(
    '10 <= x <= 100 and y >= 30', lambda x, y : 10 <= x <= 100 and y >= 30
  )
)

@set_arbitrary(
  ('string', dict(min=10)),
  ('integer', dict(max=30)))
def repeat(chars, n):
  '''
  (chars * n).split(chars) == n + 1
  '''
  repeat_string = chars * n
  return len(repeat_string.split(chars)) == n + 1

PyQCheck(verbose=True).run(10).result()
```

## Test result.

```
----- PyQCheck test results... -----
label: 10 <= x <= 100 and y >= 30
success: 10   
failure: 0
verbose:
  ☀  <lambda>(73, 2056916856135336406)
  ☀  <lambda>(41, 1673657213508719924)
  ☀  <lambda>(86, 1591870911858630638)
  ☀  <lambda>(82, 7062489949342175354)
  ☀  <lambda>(63, 4626992076240878338)
  ☀  <lambda>(43, 7448218345050658578)
  ☀  <lambda>(73, 412908156141536339)
  ☀  <lambda>(45, 3541728769292566383)
  ☀  <lambda>(36, 8830667218769458940)
  ☀  <lambda>(73, 5267004395616289964)
-----
label: (chars * n).split(chars) == n + 1
success: 10
failure: 0
verbose: 
  ☀  repeat('f87YTMsjoob', 10)
  ☀  repeat('SeFwvHNrmLAQozfKq3JE', 17)
  ☀  repeat('N7rM3F9lraN', 23)
  ☀  repeat('npHHcqBCGWrnHy2Uy', 27)
  ☀  repeat('Xhv9XXynr9x0VBvmt', 5)
  ☀  repeat('raxB8IobOeFxNnfM4Mk', 1)
  ☀  repeat('W9uDeBi6bbA', 5)
  ☀  repeat('qSxlbKKN8DM', 16)
  ☀  repeat('0ystvLvvNdcQa2uRH', 13)
  ☀  repeat('638ssJbQBgnZ65Ohfy', 23)
-----
```

# PyQCheck supports multi process.

``` python
from decimal import Decimal, getcontext
from pyqcheck.pyqcheck import PyQCheck, Arbitrary

getcontext().proc = 60

PyQCheck(process=2).add(
  Arbitrary('integer', 'integer', 'integer').property(
    'x + y + z == z + y + x',
    lambda x, y, z : x + y + z == z + y + x
  )
).add(
  Arbitrary('number', 'number', 'number').property(
    'Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)',
    lambda x, y, z : Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)
  )
).add(
  Arbitrary(
    ('string', dict(max=10))
  ).property(
    'len(chars) <= 10',
    lambda chars : len(chars) <= 10
  )
).run(100).result()
```

# Able to catch errors.

- Sample

``` python
from pyqcheck.pyqcheck import PyQCheck, Arbitrary

def ten_or_less(n):
  if n > 10:
    raise ValueError
  return True

PyQCheck(verbose=True).add(
  Arbitrary(('integer', dict(max=30))).property(
    'n <= 10 == True', ten_or_less, (ValueError,)
  )
).run(10).result()
```

- Result

```
----- PyQCheck test results... -----
label: n <= 10 == True
success: 4
failure: 0
exceptions:
  ValueError: 6
verbose:
  ☀  ten_or_less(6)
  ☃  ten_or_less(27)
  ☃  ten_or_less(27)
  ☀  ten_or_less(5)
  ☃  ten_or_less(21)
  ☀  ten_or_less(10)
  ☃  ten_or_less(18)
  ☀  ten_or_less(2)
  ☃  ten_or_less(18)
  ☃  ten_or_less(12)
-----
```

# License

MIT License

Copyright (c) <2012> Keiji Matsuzaki <futoase@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
