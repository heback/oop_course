# Device 클래스
class Device:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.status = "offline"
        self.location = location

    def activate(self):
        self.status = "online"
        print(f"Device {self.device_id} activated.")

    def deactivate(self):
        self.status = "offline"
        print(f"Device {self.device_id} deactivated.")

    def get_status(self):
        print(f"Device {self.device_id} is {self.status}.")

# Sensor 클래스
class Sensor(Device):
    def __init__(self, device_id, location, sensor_type):
        super().__init__(device_id, location)
        self.sensor_type = sensor_type
        self.data = 0.0

    def read_data(self):
        print(f"{self.sensor_type} Sensor {self.device_id} reading data: {self.data}.")

    def calibrate(self):
        print(f"{self.sensor_type} Sensor {self.device_id} calibrated.")

# Actuator 클래스
class Actuator(Device):
    def __init__(self, device_id, location, actuator_type):
        super().__init__(device_id, location)
        self.actuator_type = actuator_type
        self.state = "off"

    def activate_actuator(self):
        self.state = "on"
        print(f"{self.actuator_type} Actuator {self.device_id} activated.")

    def deactivate_actuator(self):
        self.state = "off"
        print(f"{self.actuator_type} Actuator {self.device_id} deactivated.")

# SmartThermostat 클래스 (다중 상속)
class SmartThermostat(Sensor, Actuator):
    def __init__(self, device_id, location, sensor_type, actuator_type, target_temperature):
        # super()를 사용하여 두 부모 클래스의 초기화를 수행합니다.
        Sensor.__init__(self, device_id, location, sensor_type)
        Actuator.__init__(self, device_id, location, actuator_type)
        self.target_temperature = target_temperature

    def adjust_temperature(self):
        print(f"SmartThermostat {self.device_id} adjusting temperature to {self.target_temperature}.")
        # 이곳에서 온도 조절 로직을 추가할 수 있습니다.

    def update_target_temperature(self, new_temp):
        self.target_temperature = new_temp
        print(f"SmartThermostat {self.device_id} target temperature updated to {new_temp}.")

# 다이아몬드 문제 확인 및 해결
thermostat = SmartThermostat("T1000", "Living Room", "Temperature", "Valve", 22.5)

# MRO 출력
print("MRO:", SmartThermostat.mro())

# 메서드 테스트
thermostat.activate()  # Device.activate() 호출
thermostat.get_status()  # Device.get_status() 호출
thermostat.read_data()  # Sensor.read_data() 호출
thermostat.calibrate()  # Sensor.calibrate() 호출
thermostat.activate_actuator()  # Actuator.activate_actuator() 호출
thermostat.adjust_temperature()  # SmartThermostat.adjust_temperature() 호출
thermostat.update_target_temperature(25.0)  # SmartThermostat.update_target_temperature() 호출
thermostat.deactivate_actuator()  # Actuator.deactivate_actuator() 호출
thermostat.deactivate()  # Device.deactivate() 호출
