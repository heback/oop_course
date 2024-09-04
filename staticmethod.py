class MyClass:

    cls_var = 0

    @staticmethod
    def static_method():
        print("This is a static method", MyClass.cls_var)


# 인스턴스화 없이도 호출 가능
MyClass.static_method()

a = MyClass()
a.static_method()