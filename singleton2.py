class Singleton:

    __instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if not Singleton.__instance:
            Singleton.__instance = Singleton()
        return Singleton.__instance


print(Singleton.get_instance())
print('-'*50)
print(Singleton.get_instance())