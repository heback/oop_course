from tables import users_table
from connect import engine
from sqlalchemy import select

stm = select(users_table).where(users_table.c.name == 'Joe')

with engine.connect() as conn:
    res = conn.execute(stm)

    for row in res:
        print(f'username={row.name} fullname={row.fullname}')

# print(users_table.c.name)
# print(users_table.c.fullname)
# print(users_table.c.id)