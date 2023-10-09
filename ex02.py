class Category:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name} '


class CategoryManager:

    __category_list: list[Category] = []

    def add(self, category: Category) -> 'CategoryManager':
        self.__category_list.append(category)
        return self

    def add_all(self, categories: list[Category]) -> 'CategoryManager':
        for cat in categories:
            self.add(cat)
        return self

    def __getitem__(self, i):
        if i < len(self.__category_list):
            return self.__category_list[i]
        raise Exception('부적절한 인덱스 요청')

    def __str__(self):
        for row in self.__category_list:
            if row is not None:
                print(row)
        return ''


class Subject:

    def __init__(self, category: Category, name: str):
        self.category = category
        self.name = name

    def __str__(self):
        return f'{self.category.name} {self.name} '


class SubjectManager:

    __subject_list: list[Subject] = []

    def add(self, subject: Subject) -> 'SubjectManager':
        self.__subject_list.append(subject)
        return self

    def add_all(self, subjects: list[Subject]) -> 'SubjectManager':
        for subject in subjects:
            self.add(subject)
        return self

    def __getitem__(self, i):
        if i < len(self.__subject_list):
            return self.__subject_list[i]
        raise Exception('부적절한 인덱스 요청')

    def __str__(self):
        for row in self.__subject_list:
            if row is not None:
                print(row)
        return ''


class Course:

    def __init__(self, subejct: Subject, school_year: str, semester: int):
        self.subject = subejct
        self.school_year = school_year
        self.semester = semester

    def __str__(self):
        return f'{self.subject} {self.school_year} {self.semester} '


class CourseManager:

    __course_list: list[Course] = []

    def add(self, course: Course) -> 'CourseManager':
        self.__course_list.append(course)
        return self

    def add_all(self, courses: list[Course]) -> 'CourseManager':
        for course in courses:
            self.add(course)
        return self

    def __getitem__(self, i):
        if i < len(self.__course_list):
            return self.__course_list[i]
        raise Exception('부적절한 인덱스 요청')

    def __str__(self):
        for row in self.__course_list:
            if row is not None:
                print(row)
        return ''


class Test:

    def __init__(self, course: Course, test_type:str, test_score: float):
        self.course = course
        self.test_type = test_type
        self.test_score = test_score

    def __str__(self):
        return f'{self.course} {self.test_type} {self.test_score} '


class TestManager:

    __test_list: list[Test] = []

    def add(self, test: Test) -> 'TestManager':
        self.__test_list.append(test)
        return self

    def add_all(self, tests: list[Test]) -> 'TestManager':
        for test in tests:
            self.add(test)
        return self

    def __getitem__(self, i):
        if i < len(self.__test_list):
            return self.__test_list[i]
        raise Exception('부적절한 인덱스 요청')

    def __str__(self):
        for row in self.__test_list:
            if row is not None:
                print(row)
        return ''


class Student:

    def __init__(self, name: str, grade: int, class_no: int):
        self.name = name
        self.grade = grade
        self.class_no = class_no

    def __str__(self):
        return f'{self.name} {self.grade} {self.class_no} '


class StudentManager:

    __student_list: list[Student] = []

    def add(self, student: Student) -> 'StudentManager':
        self.__student_list.append(student)
        return self

    def add_all(self, students: list[Student]) -> 'StudentManager':
        for student in students:
            self.add(student)
        return self

    def __getitem__(self, i):
        if i < len(self.__student_list):
            return self.__student_list[i]
        raise Exception('부적절한 인덱스 요청')

    def __str__(self):
        for row in self.__student_list:
            if row is not None:
                print(row)
        return ''


class CourseEnroll:

    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course

    def __str__(self):
        return f'{self.student} {self.course} '


class CourseEnrollManager:

    __course_enroll_list: list[CourseEnroll] = []

    def add(self, course_enroll: CourseEnroll) -> 'CourseEnrollManager':
        self.__course_enroll_list.append(course_enroll)
        return self

    def add_all(self, course_enrolls: list[CourseEnroll]) -> 'CourseEnrollManager':
        for course_enroll in course_enrolls:
            self.add(course_enroll)
        return self

    def __getitem__(self, i):
        if i < len(self.__course_enroll_list):
            return self.__course_enroll_list[i]
        raise Exception('부적절한 인덱스 요청')

    def __str__(self):
        for row in self.__course_enroll_list:
            if row is not None:
                print(row)
        return ''


class TestEnroll:

    def __init__(self, test: Test, student: Student, score: float):
        self.test = test
        self.student = student
        self.score = score

    def __str__(self):
        return f'{self.test} {self.student} {self.score} '


class TestEnrollManager:

    __test_enroll_list: list[TestEnroll] = []

    def add(self, test_enroll: TestEnroll) -> 'TestEnrollManager':
        self.__test_enroll_list.append(test_enroll)
        return self

    def add_all(self, test_enrolls: list[TestEnroll]) -> 'TestEnrollManager':
        for test_enroll in test_enrolls:
            self.add(test_enroll)
        return self

    def __getitem__(self, i):
        if i < len(TestEnrollManager.__test_enroll_list):
            return TestEnrollManager.__test_enroll_list[i]
        raise Exception('부적절한 인덱스 요청')

    def __str__(self):
        for row in self.__test_enroll_list:
            if row is not None:
                print(row)
        return ''


def main():

    categories = CategoryManager().add_all([
        Category('필수과정'),
        Category('기본선택'),
        Category('심화선택')
    ])

    subjects = SubjectManager().add(
        Subject(categories[0], '정보과학')).add_all([
        Subject(categories[0], '프로그래밍실습1'),
        Subject(categories[0], '프로그래밍실습2')
    ]).add_all([
        Subject(categories[1], '자료구조'),
        Subject(categories[1], '객체지향프로그래밍')
    ]).add(Subject(categories[2], '알고리즘'))

    courses = CourseManager().add_all([
        Course(subjects[0], '2023', '1학기'),
        Course(subjects[1], '2023', '1학기'),
        Course(subjects[2], '2023', '2학기'),
        Course(subjects[3], '2023', '1학기'),
        Course(subjects[4], '2023', '2학기')
    ])

    students = StudentManager().add_all([
        Student('홍길동', 1, 1),
        Student('유관순', 2, 1),
        Student('홍범도', 2, 2)
    ]).add(
        Student('이순신', 1, 2)
    )

    course_enrolls = CourseEnrollManager().add_all([
        CourseEnroll(students[0], courses[0]),
        CourseEnroll(students[1], courses[1]),
        CourseEnroll(students[1], courses[2]),
        CourseEnroll(students[2], courses[2]),
        CourseEnroll(students[2], courses[3]),
    ])

    tests = TestManager().add_all([
        Test(courses[0], '중간고사', 100),
        Test(courses[0], '기말고사', 100),
        Test(courses[1], '중간고사', 100),
        Test(courses[1], '기말고사', 100)
    ])

    test_enrolls = TestEnrollManager().add_all([
        TestEnroll(tests[0], students[0],80),
        TestEnroll(tests[1], students[0], 85),
        TestEnroll(tests[2], students[1], 90),
        TestEnroll(tests[3], students[1], 95)
    ])

    print('교육과정 구분')
    print(categories)
    print('교과목')
    print(subjects)
    print('교육과정개설')
    print(courses)
    print('학생')
    print(students)
    print('수강')
    print(course_enrolls)
    print('시험')
    print(tests)
    print('응시')
    print(test_enrolls)


if __name__ == '__main__':
    main()
