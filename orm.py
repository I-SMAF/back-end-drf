import sqlite3


class DataBase:
    def __init__(self, name):
        self.tables = []
        self.connection = sqlite3.connect(f'{name}.db')
        self.cursor = self.connection.cursor()

    def try_add_table(self, name):
        try:
            self.cursor.execute(f"""
                CREATE TABLE {name} (
                id INTEGER PRIMARY KEY);
                """)
        except:
            pass

    def try_add_columns(self, table, **kwargs):
        for name_of_column, type_of_column in kwargs.items():
            try:
                self.cursor.execute(f"""ALTER TABLE {table.name} ADD COLUMN {name_of_column} {type_of_column};""")
                self.connection.commit()
            except:
                pass

    def get_table_info(self, table):
        self.cursor.execute(f"""PRAGMA table_info({table.name});""")
        return self.cursor.fetchall()

    def get_table_objects(self, table):
        self.cursor.execute(f"""SELECT * FROM {table.name};""")
        return self.cursor.fetchall()

    def get_table_object(self, table, name_of_column, value_of_column):
        self.cursor.execute(f"""
            SELECT * FROM {table.name}
            WHERE {name_of_column} = {value_of_column};
            """)
        return self.cursor.fetchall()

    def create_table_object(self, table, *args):
        parametors = ""
        for ele in args:
            if isinstance(ele, str):
                parametors += "'" + str(ele) + "'" + ','
            else:
                parametors += str(ele) + ','
        parametors = parametors[:-1]
        self.cursor.execute(f"""
            INSERT INTO {table.name}({','.join(table.colums.keys())})
            VALUES ({parametors});
            """)
        self.connection.commit()

    def update_table_object(self, table, name_of_column, value_of_column, *args):
        for index, column in enumerate(list(table.colums.keys())[1:]):
            self.cursor.execute(f"""
                   UPDATE {table.name} SET {column} = {args[index] if isinstance(args[index], int) else "'" + args[index] + "'"}
                   WHERE {name_of_column} = {value_of_column};
                   """)
            self.connection.commit()

    def delete_table_object(self, table, name_of_column, value_of_column):
        self.cursor.execute(f"""DELETE FROM {table.name} 
                WHERE {name_of_column} = {value_of_column}""")
        self.connection.commit()

    def __delete__(self, instance):
        self.cursor.close()
        self.connection.close()
        super().__delete__(self, instance)


class Table:
    def __init__(self, name, database):
        self.colums = {}
        self.database = database
        self.name = name
        self.database.try_add_table(name)
        for column in self.database.get_table_info(self):
            self.colums[column[1]] = column[2]

    def add_colums(self, **kwargs):
        for name_of_column, type_of_column in kwargs.items():
            self.colums[name_of_column] = type_of_column
        self.database.try_add_columns(self, **self.colums)

    def get_objects(self):
        return self.database.get_table_objects(self)

    def get_object(self, name_of_column, value_of_column):
        return self.database.get_table_object(self, name_of_column, value_of_column)

    def create_object(self, *args):
        self.database.create_table_object(self, *args)

    def update_object(self, name_of_column, value_of_column, *args):
        self.database.update_table_object(self, name_of_column, value_of_column, *args)

    def delete_object(self, name_of_column, value_of_column):
        self.database.delete_table_object(self, name_of_column, value_of_column)


db = DataBase('test')
pets = Table('pets', db)
columns = {'name': 'TEXT', 'color': 'TEXT', }
pets.add_colums(**columns)
print(pets.colums.keys())
pets.create_object(1, 'alica', 'white')
print(pets.get_object('id', 1))
pets.update_object('id', 1, 'Ben', 'black')
print(pets.get_object('id', 1))
pets.delete_object('id', 1)
print(pets.get_object('id', 1))
