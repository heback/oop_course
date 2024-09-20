# 서브시스템 클래스들
class CPU:
    def freeze(self):
        print("CPU: Freezing processor...")

    def jump(self, position):
        print(f"CPU: Jumping to position {position}...")

    def execute(self):
        print("CPU: Executing instructions...")

class Memory:
    def load(self, position, data):
        print(f"Memory: Loading data at position {position}...")

class HardDrive:
    def read(self, lba, size):
        print(f"HardDrive: Reading {size} bytes from LBA {lba}...")
        return b'Data from Hard Drive'

# 퍼사드 클래스
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        print("ComputerFacade: Starting computer...")
        self.cpu.freeze()
        data = self.hard_drive.read(0, 1024)
        self.memory.load(0, data)
        self.cpu.jump(0)
        self.cpu.execute()
        print("ComputerFacade: Computer started successfully.")

# 클라이언트 코드
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()  # 복잡한 부팅 과정을 단순화하여 호출

