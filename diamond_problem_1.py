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
        Manager.__init__(self, name, salary, bonus)
        DepartmentHead.__init__(self, name, salary, department_budget)


# 사용 예제
senior_manager = SeniorManager("Alice", 70000.0, 10000.0, 50000.0)

print(senior_manager.get_salary())
# 다이아몬드 문제로 인해 어떤 get_salary 메서드가 호출될지 모호함
