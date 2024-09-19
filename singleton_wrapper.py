def singleton(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            print("새로운 싱글톤 인스턴스를 생성합니다.")
            _instance[cls] = cls(*args, **kwargs)
        else:
            print("기존 싱글톤 인스턴스를 반환합니다.")
        return _instance[cls]
    return wrapper

@singleton
class Singleton:
    def __init__(self):
        pass

# 사용 예시
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # 출력: True

