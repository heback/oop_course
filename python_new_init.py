class Point:

    # __init__이 실행되기 전에 항상 __new__가 먼저 실행되며, 이 때 객체에 메모리가 할당
    def __new__(cls, *args, **kwargs):
        print('From __new__')
        print(cls)
        print(args)
        print(kwargs)

        obj = super().__new__(cls)
        print('obj: ', obj)
        return obj

    # __init__ 메소드는 클래스 인스터스 형태인 객체(Object)가 생성(Created/Instantiated)되어
    # 초기화(Initialized)되는 즉시 호출(Called)되기는 합니다만,
    # 객체에 메모리를 할당하지 않는특수한 메소드이다.
    def __init__(self, x=0, y=-0):
        print('From __init__')
        self.x = x
        self.y = y


p1 = Point(3, 4)
print(p1)