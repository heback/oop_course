import logging
from logging.handlers import RotatingFileHandler

class LoggerSingleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)

        # 핸들러 설정 (UTF-8 인코딩)
        handler = RotatingFileHandler(
            "app.log",
            maxBytes=1000000,
            backupCount=5,
            encoding='utf-8'
        )
        handler.setLevel(logging.DEBUG)

        # 포맷터 설정
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - '
            '%(levelname)s - %(filename)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)

        # 핸들러 추가
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

# 사용 예시
if __name__ == "__main__":
    logger = LoggerSingleton().get_logger()
    logger.debug("디버그 메시지입니다.")
    logger.info("정보 메시지입니다.")
    logger.warning("경고 메시지입니다.")
    logger.error("에러 메시지입니다.")
    logger.critical("치명적인 에러 메시지입니다.")

