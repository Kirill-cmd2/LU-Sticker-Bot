from sqlite3 import connect


class MyDatabase:
    def __init__(self, path_to_db = 'main.db'):#will this file create in this directory?
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone = False, fetchall = False, commit = False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()

        cursor.execute(sql, parameters)

        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()

        connection.close()
        return data


    def create_table(self):
        sql = """
        CREATE TABLE Users (
        id int NOT NULL,
        stickerpack_name varchar(255),
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit = True)

    def add_user(self, id: int, name: str = None):
        sql = "INSERT INTO Users(id, stickerpack_name) VALUES(?, ?)"
        parameters = (id, name)
        self.execute(sql, parameters = parameters, commit = True)
    
    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall = True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone = True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone = True)


    def add_stickerpack_name(self, name: str, id: int):
        sql = "UPDATE Users SET stickerpack_name=? WHERE id=?"#
        return self.execute(sql, parameters = (name, id), commit = True)


    def delete_user(self, id):
        sql = "DELETE FROM Users WHERE id=?"
        self.execute(sql, parameters = id, commit = True)

        return "I delete a user whom have the same ID with which you sent me"

    def delete_all_users(self):
        self.execute("DELETE FROM Users WHERE True")
        return "I delete all of them!"


def logger(statement):
    print(f"""
    /\/\/\/\/\/\/\/
    executing:
    {statement}
    /\/\/\/\/\/\/\/
""")