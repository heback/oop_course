class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> None:
        print(f"{self.name} is working.")

    def get_salary(self) -> float:
        return self.salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self) -> float:
        return super().get_salary() + self.bonus


class DepartmentHead(Employee):
    def __init__(self, name: str, salary: float, department_budget: float):
        super().__init__(name, salary)
        self.department_budget = department_budget

    def get_salary(self) -> float:
        return super().get_salary() + (self.department_budget * 0.1)


class SeniorManager(Manager, DepartmentHead):
    def __init__(self, name: str, salary: float, bonus: float, department_budget: float):
        # 직접적으로 Manager와 DepartmentHead를 초기화
        Manager.__init__(name, salary, bonus)
        DepartmentHead.__init__(name, salary, department_budget)

    def get_salary(self) -> float:
        base_salary = super().get_salary(self)  # Manager의 get_salary 호출
        return base_salary + (self.department_budget * 0.1)  # DepartmentHead의 추가 급여 계산


# 사용 예제
senior_manager = SeniorManager("Alice", 70000.0, 10000.0, 50000.0)

print(senior_manager.get_salary())  # Output: 87000.0
