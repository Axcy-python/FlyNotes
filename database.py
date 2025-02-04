import sqlite3


class DB:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()


    @classmethod
    def execute(cls, query, params=()):
        cls.cursor.execute(query, params)
        cls.connection.commit()
        return cls.cursor
    


class Model:
    fields = {} #key = column name, value = column type (name: TEXT)
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    @classmethod
    def create_table(cls):
        columns = ", ".join([f"{k} {v}" for k, v in cls.fields.items()])
        query = f"CREATE TABLE IF NOT EXISTS {cls.__name__.lower()} (id INTEGER PRIMARY KEY, {columns})"
        DB.execute(query)


    @classmethod
    def create(cls, **kwargs):
        cls.create_table()
        keys = ", ".join(kwargs.keys())
        values = ", ".join(["?" for _ in kwargs])
        query = f"INSERT INTO {cls.__name__.lower()} ({keys}) VALUES ({values})"
        DB.execute(query, tuple(kwargs.values()))
        return cls(**kwargs)
    

    @classmethod
    def get(cls, record_id=None):
        cls.create_table()
        if record_id:
            query = f"SELECT * FROM {cls.__name__.lower()} WHERE id = ?"
            result = DB.execute(query, (record_id,)).fetchone()
            return cls(**dict(zip(["id"] + list(cls.fields.keys()), result))) if result else None
        else:
            query = f"SELECT * FROM {cls.__name__.lower()}"
            results = DB.execute(query).fetchall()
            return [cls(**dict(zip(["id"] + list(cls.fields.keys()), row))) for row in results]
    

    @classmethod
    def filter(cls, **conditions):
        condition_str = " AND ".join([f"{k} = ?" for k in conditions.keys()])
        query = f"SELECT * FROM {cls.__name__.lower()} WHERE {condition_str}"
        results = DB.execute(query, tuple(conditions.values())).fetchall()
        return [cls(**dict(zip(["id"] + list(cls.fields.keys()), row))) for row in results]
    

    def update(self, **kwargs):
        updates = ", ".join([f"{k} = ?" for k in kwargs.keys()])
        query = f"UPDATE {self.__class__.__name__.lower()} SET {updates} WHERE id = ?"
        DB.execute(query, tuple(kwargs.values()) + (self.id,))
        for key, value in kwargs.items():
            setattr(self, key, value)

    
    def delete(self):
        query = f"DELETE FROM {self.__class__.__name__.lower()} WHERE id = ?"
        DB.execute(query, (self.id,))


    def serialize(self) -> dict:
        return self.__dict__
    

    @classmethod
    def serialize_objs(cls):
        return [obj.__dict__ for obj in cls.get()]
