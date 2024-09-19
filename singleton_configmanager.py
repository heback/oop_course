import json

class ConfigManager:
    _instance = None
    _config = None

    def __new__(cls, config_file='config.json'):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._load_config(config_file)
        return cls._instance

    def _load_config(self, config_file):
        with open(config_file, 'r') as f:
            self._config = json.load(f)

    def get_config(self, key, default=None):
        return self._config.get(key, default)

# 사용 예시
if __name__ == "__main__":
    # config.json 파일이 있다고 가정
    config1 = ConfigManager()
    db_host = config1.get_config('database_host')
    db_port = config1.get_config('database_port')
    db_user = config1.get_config('database_user')
    db_password = config1.get_config('database_password')
    api_key = config1.get_config('api_key')
    log_level = config1.get_config('log_level')
    max_conn = config1.get_config('max_connections')

    print(f"데이터베이스 호스트: {db_host}")
    print(f"데이터베이스 포트: {db_port}")
    print(f"데이터베이스 사용자: {db_user}")
    print(f"데이터베이스 비밀번호: {db_password}")
    print(f"API 키: {api_key}")
    print(f"로그 레벨: {log_level}")
    print(f"최대 연결 수: {max_conn}")

    config2 = ConfigManager()
    print(config1 is config2)  # 출력: True

