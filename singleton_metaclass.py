class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            print("새로운 싱글톤 인스턴스를 생성합니다.")
            cls._instance = super().__call__(*args, **kwargs)
        else:
            print("기존 싱글톤 인스턴스를 반환합니다.")
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        pass

# 사용 예시
if __name__ == "__main__":
    s1 = Singleton()  # 새로운 인스턴스 생성
    s2 = Singleton()  # 기존 인스턴스 반환
    print(s1 is s2)  # 출력: True

