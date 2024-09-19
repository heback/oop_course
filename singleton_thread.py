import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()  # 클래스 레벨의 락 객체

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print("새로운 싱글톤 인스턴스를 생성합니다.")
                    cls._instance = super().__new__(cls)
        else:
            print("기존 싱글톤 인스턴스를 반환합니다.")
        return cls._instance

    def __init__(self):
        pass

# 사용 예시
def create_singleton():
    singleton = Singleton()
    print(f"싱글톤 인스턴스 ID: {id(singleton)}")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=create_singleton)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

