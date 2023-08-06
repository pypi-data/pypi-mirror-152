# cdict

This is a small library for creating lists of dictionaries combinatorially, for config/hyperparameter management.

## Installation

`pip install cdict`

## Usage

It's most easily understood by example!

```python
from cdict import cdict

c1 = cdict.dict(a=5, b=3)
assert c1.dicts() == [dict(a=5, b=3)]

# nest cdicts
c2 = cdict.dict(nested=c1, c=4)
assert c2.dicts() == [dict(nested=dict(a=5, b=3), c=4)]

# "add" cdicts by union-ing the set of dicts
c3 = c1 + c2
assert c3.dicts() == [
    dict(a=5, b=3),
    dict(nested=dict(a=5, b=3), c=4)
]

# and most importantly, combinatorially multiply
c4 = c1 * c2
assert c4.dicts() == [
    dict(a=5, b=3, nested=dict(a=5, b=3), c=4)
]
```
