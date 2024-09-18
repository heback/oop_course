
# 싱글턴 패턴 구현
# 1. 하나의 Singleton 클래스 인스턴스를 생성한다.
# 2. 이미 생성된 인스턴스가 있다면 재사용한다.

class Singleton:
    _instance = None  # 클래스 변수로 인스턴스 저장

    def __new__(cls, *args, **kwargs):
        # if not cls._instance:
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
if s1 is s2:
    print("Singleton exists")

