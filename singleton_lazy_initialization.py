class Singleton:
    _instance = None  # 초기에는 인스턴스가 없음

    def __new__(cls, *args, **kwargs):
        if Singleton._instance is not None:
            raise Exception("싱글톤 클래스는 한 번만 생성할 수 있습니다.")
        else:
            print("새로운 싱글톤 인스턴스를 생성합니다.")
            Singleton._instance = super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()  # 새로운 인스턴스 생성
        else:
            print("기존 싱글톤 인스턴스를 반환합니다.")
        return cls._instance


# 사용 예시
if __name__ == "__main__":
    s1 = Singleton.get_instance()  # 새로운 인스턴스 생성
    s2 = Singleton.get_instance()  # 기존 인스턴스 반환
    print(s1 is s2)  # 출력: True

