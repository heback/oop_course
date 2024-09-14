class Employee:
    def __init__(self, name='', salary=0.0, **kwargs):
        print(f"Employee init name:{name}, salary:{salary}")
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

    def get_salary(self) -> float:
        res = self.salary
        return res


class Manager(Employee):
    def __init__(self, bonus=0.0, **kwargs):
        print(f"Manager init bonus:{bonus}")
        self.bonus = bonus
        super().__init__(**kwargs)

    def get_salary(self) -> float:
        res = super().get_salary() + self.bonus
        return res


class DepartmentHead(Employee):
    def __init__(self, department_budget=0.0, **kwargs):
        print(f"DepartmentHead init department_budget:{department_budget}")
        self.department_budget = department_budget
        super().__init__(**kwargs)

    def get_salary(self) -> float:
        res = super().get_salary() + (self.department_budget * 0.1)
        return res



class SeniorManager(Manager, DepartmentHead):
    def __init__(self, **kwargs):
        print("SeniorManager init")
        super().__init__(**kwargs)

    def get_salary(self) -> float:
        res = super().get_salary()
        return res


# SeniorManager 객체 생성
senior_manager = SeniorManager(name="Alice", salary=70000,
                               bonus=1000, department_budget=50000)
print(senior_manager.get_salary())
print(SeniorManager.__mro__)

# 실행 결과
# SeniorManager init
# Manager init bonus:1000
# DepartmentHead init department_budget:50000
# Employee init name:Alice, salary:70000
# 76000.0
# (<class '__main__.SeniorManager'>, <class '__main__.Manager'>, <class '__main__.DepartmentHead'>, <class '__main__.Employee'>, <class 'object'>)