class SingletonMeta(type):
  _instance = None

  def __call__(cls, *args, **kwargs):
    if cls._instance is None:
      print("새로운 싱글톤 인스턴스를 생성합니다.")
      cls._instance = super().__call__(*args, **kwargs)
      print(cls.__name__, cls._instance)
    else:
      print("기존 싱글톤 인스턴스를 반환합니다.")
    return cls._instance

class Singleton3(metaclass=SingletonMeta):
  def __init__(self):
    pass

s1 = Singleton3()
s2 = Singleton3()
print(s1 is s2)

#___________여기까지는 ppt 코드___________

class Singleton4(metaclass=SingletonMeta):
  def __init__(self):
    pass

s3 = Singleton4()
print(s1 is s3)