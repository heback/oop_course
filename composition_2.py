# Wheel 클래스 정의
class Wheel:
    def roll(self):
        print("The wheel is rolling.")

# Engine 클래스 정의
class Engine:
    def start(self):
        print("Engine started.")

# Car 클래스 정의 (컴포지션 사용)
class Car:
    def __init__(self):
        # 엔진을 포함함
        self.engine = Engine()
        # 바퀴 4개 포함
        self.wheels = [Wheel() for _ in range(4)]

    def drive(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.roll()
        print("Car is driving...")

# Car 객체 생성 및 메서드 호출
my_car = Car()
my_car.drive()

