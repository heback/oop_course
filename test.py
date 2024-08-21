class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):

        super().method()
        print("Method in B")

class C(A):
    def method(self):

        super().method()
        print("Method in C")

class D(B, C):
    def method(self):

        super().method()
        print("Method in D")

d = D()
d.method()
