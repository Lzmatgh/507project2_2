import numpy as np

a = ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

# idx = a.index("Is it bigger than a breadbox?")
# print(idx)
b = list(a)
print(b)
c = tuple(b)
print(c)
print(a)
ab = tuple(['a', 'b'])
print(ab)
print(type(ab))

b = 'nihao'

a = f'haha {b}'
print(a)
a = ['haha', float(2.3)]
print(type(a[0]))