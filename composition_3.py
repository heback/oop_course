# CPU 클래스 정의
class CPU:
    def execute(self):
        print("CPU is executing instructions.")

# RAM 클래스 정의
class RAM:
    def load(self):
        print("RAM is loading data.")

# HardDrive 클래스 정의
class HardDrive:
    def read(self):
        print("Hard Drive is reading data.")

# Computer 클래스 정의 (컴포지션 사용)
class Computer:
    def __init__(self):
        self.cpu = CPU()  # CPU 포함
        self.ram = RAM()  # RAM 포함
        self.hard_drive = HardDrive()  # Hard Drive 포함

    def run(self):
        self.cpu.execute()
        self.ram.load()
        self.hard_drive.read()

# Computer 객체 생성 및 메서드 호출
my_computer = Computer()
my_computer.run()

