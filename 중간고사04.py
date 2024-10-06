import pickle

# 싱글톤 패턴 - AdminManager
class AdminManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AdminManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'courses'):
            self.courses = []

    def create_course(self, title, teacher):
        course = CourseFactory.create_course(title, teacher)
        self.courses.append(course)

    def register_student(self, course, student):
        course.add_student(student)

    def save_state(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            print("System state saved.")
        except Exception as e:
            print(f"Error saving state: {e}")

    def load_state(self, filename):
        try:
            with open(filename, 'rb') as f:
                loaded_manager = pickle.load(f)
                self.__dict__.update(loaded_manager.__dict__)
            print("System state loaded.")
        except FileNotFoundError:
            print("No saved state found.")
        except Exception as e:
            print(f"Error loading state: {e}")

# 팩토리 패턴 - CourseFactory 및 StudentFactory
class CourseFactory:
    @staticmethod
    def create_course(title, teacher):
        return Course(title, teacher)

class StudentFactory:
    @staticmethod
    def create_student(name, student_id):
        return Student(name, student_id)

# 퍼사드 패턴 - LectureSystem
class LectureSystem:
    def __init__(self):
        self.attendance_system = AttendanceSystem()
        self.lecture_progress = LectureProgress()
        self.record_system = RecordSystem()

    def start_lecture(self, course):
        self.attendance_system.check_attendance(course)
        self.lecture_progress.begin(course)
        self.record_system.record_attendance(course)

# 서브 시스템들
class AttendanceSystem:
    def check_attendance(self, course):
        print(f"Checking attendance for {course.title}...")

class LectureProgress:
    def begin(self, course):
        print(f"Starting lecture: {course.title}")

class RecordSystem:
    def record_attendance(self, course):
        print(f"Recording attendance for {course.title}")

# 강의와 학생 클래스
class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

# 실행 예시
admin_manager = AdminManager()

# 강의 생성 및 학생 등록
course = CourseFactory.create_course("Python Programming", "Dr. John")
student1 = StudentFactory.create_student("Alice", 101)
admin_manager.register_student(course, student1)

# 강의 진행
lecture_system = LectureSystem()
lecture_system.start_lecture(course)

# 시스템 저장 및 복구
admin_manager.save_state('system_state.pkl')
admin_manager.load_state('system_state.pkl')
