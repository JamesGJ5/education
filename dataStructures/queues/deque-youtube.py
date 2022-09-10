import collections
from collections import deque

d = deque("hello")
print(d)

d.append("4")
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d = deque("hello")
print(d)

d.extend("123")
print(d)

d.extendleft("abc")
print(d)

d.extendleft("abc"[::-1])
print(d)

d.rotate(-1)
print(d)

d.rotate(1)
print(d)

d = deque("hello", maxlen = 5)
print(d)

d.append(1)
print(d)

d.extend("2345")
print(d)

print(d.maxlen)

# Can't change maxlen
# d.maxlen = 5