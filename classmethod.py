class MyClass:
    class_variable = 0

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1
        print(f"Class variable is now {cls.class_variable}")


# 클래스 메서드를 클래스 이름으로 호출
MyClass.increment_class_variable()
MyClass.increment_class_variable()


# 인스턴스를 통해서도 호출 가능
obj = MyClass()
obj.increment_class_variable()

