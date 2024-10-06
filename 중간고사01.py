from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    employee_id: int
    department: str = "General"
    salary: int = 0
    skills: list = None
    employee_count = 0

    def __post_init__(self):
        self.skills = self.skills or []
        Employee.increment_employee_count()

    @classmethod
    def increment_employee_count(cls):
        cls.employee_count += 1

    def add_skill(self, skill):
        self.skills.append(skill)

    def change_department(self, new_department):
        self.department = new_department

    def display_employee_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, "
              f"Salary: {self.salary}, Skills: {', '.join(self.skills)}")

    @classmethod
    def compare_salary(cls, emp1, emp2):
        if emp1.salary > emp2.salary:
            return emp1
        return emp2

    @classmethod
    def display_employee_count(cls):
        print(f"Employee count: {cls.employee_count}")


# 실행 예시
emp1 = Employee("Alice", 101, salary=50000)
emp2 = Employee("Bob", 102, salary=60000)
emp2.change_department('HR')
emp3 = Employee("Charlie", 103, "HR", 55000, ['Excel'])

emp1.add_skill("Python")
emp1.add_skill("Data Analysis")
emp2.add_skill("Java")
emp2.add_skill("Project Management")

emp1.display_employee_info()
emp2.display_employee_info()
emp3.display_employee_info()

# 급여 비교
higher_salary_emp = Employee.compare_salary(emp1, emp2)
print(f"Higher salary: {higher_salary_emp.name}")

# 직원수 출력
Employee.display_employee_count()
