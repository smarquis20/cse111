def func1():
  a=1
def func2():
  a=2
  func1()
  return a
a=0
print(func2())