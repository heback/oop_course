from typing import Optional

class Category:

    def __init__(self, name: str):
        self.name = name


class CategoryManager:

    __category_list = list[Category] = []

    @staticmethod
    def add(cls, category: Category) -> Optional['CategoryManager', None]:
        cls.__category_list.append(category)
        return cls


    @staticmethod
    def add_all(cls, categories: list[Category]) -> 'CategoryManager':
        for cat in categories:
            cls.add(cat)
        return cls

    def __str__(self):
        for row in self.__category_list:
            print(row)


class Subject:

    def __init__(self, category: Category, name: str):
        self.category = category
        self.name = name


class SubjectManager:

    __subject_list = list[Subject] = []

    @staticmethod
    def add(cls, subject: Subject) -> 'SubjectManager':
        cls.__subject_list.append(subject)
        return cls

    @staticmethod
    def add_all(cls, subjects: list[Subject]) -> 'SubjectManager':
        for subject in subjects:
            cls.add(subject)
        return cls


class Course:

    def __init__(self, subejct: Subject, school_year: str, semester: int):
        self.subject = subejct
        self.school_year = school_year
        self.semester = semester


class CourseManager:

    __course_list = list[Course] = []

    @staticmethod
    def add(cls, course: Course) -> 'CourseManager':
        cls.__course_list.append(course)
        return cls

    @staticmethod
    def add_all(cls,courses: list[Course]) -> 'CourseManager':
        for course in courses:
            cls.add(course)
        return cls


class Test:

    def __init__(self, course: Course, test_type:str, test_score: float):
        self.course = course
        self.test_type = test_type
        self.test_score = test_score


class TestManager:

    __test_list = list[Test] = []

    @staticmethod
    def add(cls, test: Test) -> 'TestManager':
        cls.__test_list.append(test)
        return cls

    @staticmethod
    def add_all(cls, tests: list[Test]) -> 'TestManager':
        for test in tests:
            cls.add(test)
        return cls


class Student:

    def __init__(self, name: str, grade: int, class_no: int):
        self.name = name
        self.grade = grade
        self.class_no = class_no


class StudentManager:

    __student_list = list[Student] = []

    @staticmethod
    def add(cls, student: Student) -> 'StudentManager':
        cls.__student_list.append(student)
        return cls

    @staticmethod
    def add_all(cls, students: list[Student]) -> 'StudentManager':
        for student in students:
            cls.add(student)
        return cls


class CourseEnroll:

    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course


class CourseEnrollManager:

    __course_enroll_list = list[CourseEnroll] = []

    @staticmethod
    def add(cls, course_enroll: CourseEnroll) -> 'CourseEnrollManager':
        cls.__course_enroll_list.append(course_enroll)
        return cls

    @staticmethod
    def add_all(cls, course_enrolls: list[CourseEnroll]) -> 'CourseEnrollManager':
        for course_enroll in course_enrolls:
            cls.add(course_enroll)
        return cls


class TestEnroll:

    def __init__(self, test: Test, student: Student, score: float):
        self.test = test
        self.student = student
        self.score = score


class TestEnrollManager:

    __test_enroll_list = list[TestEnroll] = []

    @staticmethod
    def add(cls, test_enroll: TestEnroll) -> 'TestEnrollManager':
        cls.__test_enroll_list.append(test_enroll)
        return cls

    @staticmethod
    def add_all(cls, test_enrolls: list[TestEnroll]) -> 'TestEnrollManager':
        for test_enroll in test_enrolls:
            cls.add(test_enroll)
        return cls


def main():

    categories = CategoryManager.add_all([Category('필수과정'), Category('기본선택'), Category('심화선택')])
    subjects = SubjectManager.add(Subject(categories[0], '정보과학')).add_all(
        [
            Subject(categories[0], '정보과학'),
            Subject(categories[0], '프로그래밍실습1'),
            Subject(categories[0], '프로그래밍실습2')
        ]
    ).add_all(
        [
            Subject(categories[1], '자료구조'),
            Subject(categories[1], '객체지향프로그래밍')
        ]
    ).add(Subject(categories[2], '알고리즘'))

    courses = CourseManager.add_all([

    ])


if __name__ == '__main__':
    main()
