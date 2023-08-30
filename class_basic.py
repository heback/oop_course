class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

print(a)
print(b)
print(a is b)

class Point:
    pass

p1 = Point()
p2 = Point()

p1.x = 1
p1.y = 2

p2.x = 3
p2.y = 4

print(p1.x, p1.y)
print(p2.x, p2.y)

class Point:

    def reset(self): # self는 관례적인 표기임
        self.x = 0
        self.y = 0

p = Point()
p.x = 1
p.y = 2
p.reset()
print(p.x, p.y)


