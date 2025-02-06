from peewee import SqliteDatabase, Model, PrimaryKeyField, CharField, TextField, ForeignKeyField


db: SqliteDatabase = SqliteDatabase(database="database.db")


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)


    class Meta:
        database = db
        order_by = "id"


class Folder(BaseModel):
    folder_name:CharField = CharField(max_length=16)

    class Meta:
        db_table = "folders"


class Note(BaseModel):
    title = CharField(max_length=255)
    content = TextField()
    folder_id = ForeignKeyField(Folder)

    class Meta:
        db_table = "notes"