class Person:
    def __init__(self, name='', email='', **kwargs):
        self.name = name
        self.email = email
        print(f"Person init: {self.name}, {self.email}")
        super().__init__(**kwargs)

    def introduce(self):
        print(f"안녕하세요, 저는 {self.name}입니다.")

class Student(Person):
    def __init__(self, student_id='', **kwargs):
        self.student_id = student_id
        print(f"Student init: ID={self.student_id}")
        super().__init__(**kwargs)

    def enroll_course(self, course_name):
        print(f"{self.name}님이 {course_name} 강좌에 등록했습니다.")

class Instructor(Person):
    def __init__(self, employee_id='', **kwargs):
        self.employee_id = employee_id
        print(f"Instructor init: 직원 ID={self.employee_id}")
        super().__init__(**kwargs)

    def assign_homework(self, homework):
        print(f"{self.name}님이 과제 '{homework}'를 배정했습니다.")

class OnlineMixin:
    def __init__(self, **kwargs):
        print("OnlineMixin init")
        super().__init__(**kwargs)

    def login(self):
        print(f"{self.name}님이 온라인으로 로그인했습니다.")

class OnsiteMixin:
    def __init__(self, location='', **kwargs):
        self.location = location
        print(f"OnsiteMixin init: 위치={self.location}")
        super().__init__(**kwargs)

    def attend_class(self):
        print(f"{self.name}님이 {self.location}에서 수업에 참석했습니다.")

class OnlineStudent(Student, OnlineMixin):
    def __init__(self, **kwargs):
        print("OnlineStudent init")
        super().__init__(**kwargs)

class OnsiteInstructor(Instructor, OnsiteMixin):
    def __init__(self, **kwargs):
        print("OnsiteInstructor init")
        super().__init__(**kwargs)

class TeachingAssistant(Student, Instructor):
    def __init__(self, **kwargs):
        print("TeachingAssistant init")
        super().__init__(**kwargs)

    def assist(self):
        print(f"{self.name}님이 조교로서 도움을 제공하고 있습니다.")


# 강의 자료 관련 클래스
class CourseMaterial:
    def __init__(self, title='', content='', **kwargs):
        self.title = title
        self.content = content
        print(f"CourseMaterial init: {self.title}")
        super().__init__(**kwargs)

    def display(self):
        print(f"강의 자료: {self.title}")

class VideoMaterial(CourseMaterial):
    def __init__(self, duration=0, **kwargs):
        self.duration = duration
        print(f"VideoMaterial init: duration={self.duration}")
        super().__init__(**kwargs)

    def play(self):
        print(f"{self.title} 비디오를 재생합니다. 길이: {self.duration}분")

class TextMaterial(CourseMaterial):
    def __init__(self, word_count=0, **kwargs):
        self.word_count = word_count
        print(f"TextMaterial init: 단어 수={self.word_count}")
        super().__init__(**kwargs)

    def read(self):
        print(f"{self.title} 텍스트를 읽습니다. 단어 수: {self.word_count}")

# 믹스인 클래스
class DownloadableMixin:
    def __init__(self, **kwargs):
        print("DownloadableMixin init")
        super().__init__(**kwargs)

    def download(self):
        print(f"{self.title}를 다운로드합니다.")

class InteractiveMixin:
    def __init__(self, **kwargs):
        print("InteractiveMixin init")
        super().__init__(**kwargs)

    def interact(self):
        print(f"{self.title}에 상호작용합니다.")

# 다중 상속 강의 자료 클래스
class InteractiveVideo(VideoMaterial, InteractiveMixin):
    def __init__(self, **kwargs):
        print("InteractiveVideo init")
        super().__init__(**kwargs)

class DownloadableText(TextMaterial, DownloadableMixin):
    def __init__(self, **kwargs):
        print("DownloadableText init")
        super().__init__(**kwargs)

# 특수 자료 클래스
class QuizMaterial(CourseMaterial, InteractiveMixin):
    def __init__(self, questions=None, **kwargs):
        if questions is None:
            questions = []
        self.questions = questions
        print(f"QuizMaterial init: 질문 수={len(self.questions)}")
        super().__init__(**kwargs)

    def display(self):
        print(f"퀴즈: {self.title}, 질문 수: {len(self.questions)}")

    def evaluate(self):
        print(f"{self.title} 퀴즈를 평가합니다.")


# 사용 예제

# OnlineStudent 인스턴스 생성
online_student = OnlineStudent(name="김학생",
                               email="student@example.com",
                               student_id="S12345")

# OnsiteInstructor 인스턴스 생성
onsite_instructor = OnsiteInstructor(name="이강사",
                                     email="instructor@example.com",
                                     employee_id="E67890",
                                     location="서울캠퍼스")

# TeachingAssistant 인스턴스 생성
teaching_assistant = TeachingAssistant(name="박조교",
                                       email="assistant@example.com",
                                       student_id="S54321",
                                       employee_id="E09876")

# 메서드 호출
online_student.introduce()
online_student.login()
online_student.enroll_course("파이썬 프로그래밍")

onsite_instructor.introduce()
onsite_instructor.attend_class()
onsite_instructor.assign_homework("프로젝트 1")

teaching_assistant.introduce()
teaching_assistant.enroll_course("데이터 사이언스")
teaching_assistant.assign_homework("과제 2")
teaching_assistant.assist()

# 강의 자료 인스턴스 생성
video = InteractiveVideo(title="파이썬 기초",
                         content="비디오 내용",
                         duration=30)
text = DownloadableText(title="데이터 구조",
                        content="텍스트 내용",
                        word_count=2000)
quiz = QuizMaterial(title="OOP 퀴즈",
                    content="퀴즈 내용",
                    questions=["Q1", "Q2", "Q3"])

# 메서드 호출
video.display()
video.play()
video.interact()

text.display()
text.read()
text.download()

quiz.display()
quiz.interact()
quiz.evaluate()