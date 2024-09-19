class DBConnection:
    def connect(self):
        pass

class MySQLConnection(DBConnection):
    def connect(self):
        print("MySQL 데이터베이스에 연결합니다.")

class PostgreSQLConnection(DBConnection):
    def connect(self):
        print("PostgreSQL 데이터베이스에 연결합니다.")

class SQLiteConnection(DBConnection):
    def connect(self):
        print("SQLite 데이터베이스에 연결합니다.")

class DBConnectionFactory:
    @staticmethod
    def get_connection(db_type):
        if db_type == "mysql":
            return MySQLConnection()
        elif db_type == "postgresql":
            return PostgreSQLConnection()
        elif db_type == "sqlite":
            return SQLiteConnection()
        else:
            raise ValueError(
                f"지원되지 않는 데이터베이스 타입입니다: "
                f"{db_type}")

# 사용 예시
if __name__ == "__main__":
    db_type = "postgresql"
    connection = DBConnectionFactory.get_connection(db_type)
    connection.connect()
    # 출력: PostgreSQL 데이터베이스에 연결합니다.

