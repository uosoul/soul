def test1():
   l = []
   for i in range(1000):
      l = l + [i]  # l += [i] 是优化了的
def test2():
   l = []
   for i in range(1000):
      l.append(i)
def test3():
   l = [i for i in range(1000)]
def test4():
   l = list(range(1000))
def test5():
   li = []
   for i in range(1000):
           li.extend([i])
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "seconds")
t5 = Timer("test4()", "from __main__ import test4")
print("extend: ",t5.timeit(number=1000), "seconds")
