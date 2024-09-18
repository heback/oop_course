class Employee:
  def __init__(self,
               name: str = '',
               salary: float = 0.0) -> None:
    print(f"Employee init name:{name}, salary:{salary}")
    self.name = name
    self.salary = salary

  def work(self) -> None:
    print(f"{self.name} is working")

  def get_salary(self) -> float:
    res = self.salary
    print('Employee: ', self.salary)
    return res

class Manager(Employee):
  def __init__(self, name: str = '', salary: float = 0.0, bonus : float = 0.0) -> None:
    print(f"Manager init name:{name}, salary:{salary}, bonus:{bonus}")
    Employee.__init__(self, name=name, salary=salary)
    self.bonus = bonus

  def get_salary(self) -> float:
    res = super().get_salary() + self.bonus
    print('Manager: ', res)
    return res

class DepartmentHead(Employee):
  def __init__(self,
               name : str = '',
               salary : float = 0.0,
               department_budget: float = 0.0) -> None:
    print(f"DepartementHead init name:{name}, salary:{salary}, department_budget{department_budget}")
    Employee.__init__(self, name=name, salary=salary)
    self.department_budget = department_budget

  def get_salary(self) -> float:
    res = super().get_salary() + (self.department_budget * 0.1)
    print('DepartmentHead: ', res)
    return res

class SeniorManager(Manager, DepartmentHead):
  def __init__(self, name: str, salary: float,
               bonus: float, department_budget: float):
    print(f"SeniorManger init name:{name}, salary:{salary}, bonus:{bonus}, department_budget:{department_budget}")
    print("Manager 초기화")
    Manager.__init__(self, name= name,
                     salary=salary, bonus=bonus)
    print("DepartmentHead 초기화")
    DepartmentHead.__init__(self, name=name,
                            salary=salary,
                            department_budget=department_budget)

    def get_salary(self) -> float:
      res = super().get_salary()
      print('SeniorManager', res)
      return res

senior_manager = SeniorManager(name="Alice", salary=70000,
                                bonus=1000, department_budget=50000)
print('SeniorManager 연봉:', senior_manager.get_salary())
print(SeniorManager.__mro__)
#
# manager = Manager(name='Jungu', salary=70000, bonus=10000)
# print(manager.get_salary())
#
# department_head = DepartmentHead(name='Eunjin', salary=70000, department_budget=130000)
# print(department_head.get_salary())
