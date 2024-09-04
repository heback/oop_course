class MyClass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name")
        self._name = value


# 인스턴스 생성
obj = MyClass("Alice")

# 메서드처럼 호출하지 않고 속성처럼 접근
print(obj.name)

# 속성처럼 값을 설정
obj.name = "Bob"
print(obj.name)

