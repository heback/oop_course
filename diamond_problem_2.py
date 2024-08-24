
class Employee:
    def __init__(self,
                 name: str = '',
                 salary: float = 0.0) -> None:
        self.name = name
        self.salary = salary

    def work(self) -> None:
        print(f"{self.name} is working.")

    def get_salary(self) -> float:
        res = self.salary
        print('Employee: ', self.salary)
        return res


class Manager(Employee):
    def __init__(self,
                 name: str = '',
                 salary: float = 0.0,
                 bonus: float = 0.0) -> None:
        super().__init__(name=name, salary=salary)
        self.bonus = bonus

    def get_salary(self) -> float:
        res = super().get_salary() + self.bonus
        print('Manager: ', res)
        return res


class DepartmentHead(Employee):
    def __init__(self,
                 name: str = '',
                 salary: float = 0.0,
                 department_budget: float = 0.0) -> None:
        super().__init__(name=name, salary=salary)
        self.department_budget = department_budget

    def get_salary(self) -> float:
        res = super().get_salary() + (self.department_budget * 0.1)
        print('DepartmentHead: ', res)
        return res


class SeniorManager(Manager, DepartmentHead):
    def __init__(self, name: str, salary: float,
                 bonus: float, department_budget: float):
        # 직접적으로 Manager와 DepartmentHead를 초기화
        Manager.__init__(self, name = name,
                         salary=salary, bonus=bonus)
        DepartmentHead.__init__(self, name=name,
                                salary=salary,
                                department_budget=department_budget)

    def get_salary(self) -> float:
        res = super().get_salary()  # Manager의 get_salary 호출
        print('SeniorManager: ', res)
        return res


# 사용 예제
senior_manager = SeniorManager(name="Alice", salary=70000.0,
                               bonus=10000.0, department_budget=50000.0)
print(senior_manager.get_salary())  # Output: 87000.0

manager = Manager(name='Jungu', salary=70000, bonus=10000)
print(manager.get_salary())

