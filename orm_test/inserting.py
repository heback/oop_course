from sqlalchemy import insert
from tables import users_table
from connect import engine


# stm = insert(users_table).values(
#     name = 'heback',
#     fullname = 'Jungu Lee'
# )
#
# with engine.connect() as conn:
#     conn.execute(stm)
#     conn.commit()

stm = insert(users_table)

with engine.connect() as conn:
    conn.execute(stm, [
        {'name': 'Joe', 'fullname': 'Joe Biden'},
        {'name': 'Sponge', 'fullname': 'Sponge Bob'}
    ])
    conn.commit()