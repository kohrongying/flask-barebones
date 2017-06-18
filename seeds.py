from app import db
from sqlalchemy import text

# quotes for user because user is a reserved word in Postgres, for other table names, can omit ""

insert_user = text(
    'INSERT INTO "user" VALUES (2,\'uhthiswillnotbehashed\')'
)

delete_user = text(
    'DELETE FROM "user"'
)

def run():
    db.engine.execute(insert_user)

def clear():
    db.engine.execute(delete_user)

