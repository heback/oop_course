from tables import users_table
from connect import engine
from sqlalchemy import delete

stm = delete(users_table).where(
    users_table.c.name == 'Jerry'
)

with engine.connect() as conn:
    conn.execute(stm)
    conn.commit()
