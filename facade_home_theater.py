# 서브시스템 클래스들
class Television:
    def on(self):
        print("TV: 전원을 켭니다.")

    def off(self):
        print("TV: 전원을 끕니다.")

class SoundSystem:
    def on(self):
        print("사운드 시스템: 전원을 켭니다.")

    def off(self):
        print("사운드 시스템: 전원을 끕니다.")

    def set_volume(self, level):
        print(f"사운드 시스템: 볼륨을 {level}로 설정합니다.")

class BluRayPlayer:
    def on(self):
        print("블루레이 플레이어: 전원을 켭니다.")

    def off(self):
        print("블루레이 플레이어: 전원을 끕니다.")

    def play(self, movie):
        print(f"블루레이 플레이어: '{movie}' 재생을 시작합니다.")

class Lights:
    def dim(self, level):
        print(f"조명: 밝기를 {level}%로 낮춥니다.")

# 퍼사드 클래스
class HomeTheaterFacade:
    def __init__(self,
                 tv,
                 sound_system,
                 blu_ray_player,
                 lights):
        self.tv = tv
        self.sound_system = sound_system
        self.blu_ray_player = blu_ray_player
        self.lights = lights

    def watch_movie(self, movie):
        print("홈 시어터: 영화 보기를 시작합니다.")
        self.lights.dim(30)
        self.tv.on()
        self.sound_system.on()
        self.sound_system.set_volume(20)
        self.blu_ray_player.on()
        self.blu_ray_player.play(movie)

    def end_movie(self):
        print("홈 시어터: 영화 보기를 종료합니다.")
        self.lights.dim(100)
        self.blu_ray_player.off()
        self.sound_system.off()
        self.tv.off()

# 클라이언트 코드
if __name__ == "__main__":
    # 서브시스템 객체 생성
    tv = Television()
    sound_system = SoundSystem()
    blu_ray_player = BluRayPlayer()
    lights = Lights()

    # 퍼사드 객체 생성
    home_theater = HomeTheaterFacade(
        tv,
        sound_system,
        blu_ray_player,
        lights)

    # 간단한 인터페이스로 영화 보기
    home_theater.watch_movie("인셉션")
    print("\n잠시 후...\n")
    home_theater.end_movie()

