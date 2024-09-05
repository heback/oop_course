# Engine 클래스 정의
class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

# Car 클래스 정의 (컴포지션 사용)
class Car:
    def __init__(self):
        # Car는 Engine을 포함함 (has-a 관계)
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving...")
        self.engine.stop()

# Car 객체 생성 및 메서드 호출
my_car = Car()
my_car.drive()

