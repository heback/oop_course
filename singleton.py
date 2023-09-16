
# 싱글턴 패턴 구현
# 1. 하나의 Singleton 클래스 인스턴스를 생성한다.
# 2. 이미 생성된 인스턴스가 있다면 재사용한다.

class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


s = Singleton()
print(s)

s1 = Singleton()
print(s1)
