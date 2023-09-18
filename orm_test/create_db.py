from orm_test.connect import engine
from orm_test.tables import users_table, comments_table, meta_obj

print(">>>CREATE DATABASE")
meta_obj.create_all(bind = engine)
