import sqlite3
from queue import Queue

class DatabaseConnectionPool:
    _instance = None

    def __new__(cls, max_connections=5):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_pool(max_connections)
        return cls._instance

    def _initialize_pool(self, max_connections):
        self._connection_pool = Queue(maxsize=max_connections)
        for _ in range(max_connections):
            conn = sqlite3.connect('example.db')
            self._connection_pool.put(conn)

    def get_connection(self):
        return self._connection_pool.get()

    def return_connection(self, conn):
        self._connection_pool.put(conn)

    def close_all_connections(self):
        while not self._connection_pool.empty():
            conn = self._connection_pool.get()
            conn.close()

# 사용 예시
if __name__ == "__main__":
    pool = DatabaseConnectionPool()
    conn1 = pool.get_connection()
    cursor = conn1.cursor()
    # 데이터베이스 작업 수행
    cursor.execute("CREATE TABLE IF NOT EXISTS "
                   "users (id INTEGER PRIMARY KEY, name TEXT)")
    conn1.commit()
    pool.return_connection(conn1)

    pool2 = DatabaseConnectionPool()
    conn2 = pool2.get_connection()
    # 또 다른 데이터베이스 작업 수행
    cursor = conn2.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)",
                   ('Alice',))
    conn2.commit()
    pool2.return_connection(conn2)

    print(pool is pool2)  # 출력: True

