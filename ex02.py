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
    def add(cls, subject: Subject) -> Optional['SubjectManager', None]:
        cls.__subject_list.append(subject)
        return cls

    @staticmethod
    def add_all(cls, subjects: list[Subject]) -> Optional['SubjectManager', None]:
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

    def add(self, course: Course):
        self.__course_list.append(course)


class Test:

    def __init__(self, course: Course, test_type:str, test_score: float):
        self.course = course
        self.test_type = test_type
        self.test_score = test_score


class TestManager:

    __test_list = list[Test] = []

    def add(self, test: Test):
        self.__test_list.append(test)


class Student:

    def __init__(self, name: str, grade: int, class_no: int):
        self.name = name
        self.grade = grade
        self.class_no = class_no


class StudentManager:

    __student_list = list[Student] = []

    def add(self, student: Student):
        self.__student_list.append(student)


class CourseEnroll:

    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course


class CourseEnrollManager:

    __course_enroll_list = list[CourseEnroll] = []

    def add(self, course_enroll: CourseEnroll):
        self.__course_enroll_list.append(course_enroll)


class TestEnroll:

    def __init__(self, test: Test, student: Student, score: float):
        self.test = test
        self.student = student
        self.score = score


class TestEnrollManager:

    __test_enroll_list = list[TestEnroll] = []

    def __add__(self, test_enroll: TestEnroll):
        self.__test_enroll_list.append(test_enroll)


def main():

    categories = CategoryManager.add_all([Category('공통필수'), Category('심화필수'), Category('심화선택')])
    subjects = SubjectManager.add(categories[0], '정보과학')




if __name__ == '__main__':
    main()
