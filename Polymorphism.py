from pathlib import Path


class AudioFile:
    ext: str

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix.lower() == self.ext:
            raise ValueError(f'Invalid file extension: {filepath.suffix}')
        self.filepath = filepath


class MP3File(AudioFile):
    ext = '.mp3'

    def play(self) -> None:
        print(f'Playing {self.filepath} as mp3')


class WAVFile(AudioFile):
    ext = '.wav'

    def play(self) -> None:
        print(f'Playing {self.filepath} as wav')


class FLACFile(AudioFile):
    ext = '.flac'

    def play(self) -> None:
        print(f'Playing {self.filepath} as flac')


class OGGFile(AudioFile):
    ext = '.ogg'

    def play(self) -> None:
        print(f'Playing {self.filepath} as ogg')


ogg = OGGFile(Path('a.ogg'))
ogg.play()
