import pymysql
from config import DB_CONFIG


class Database:
    def __init__(self):
        """Подключаемся к БД"""
        self.conn = pymysql.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()
        print("Подключились")



    def create_table(self, table_name, columns):
        # автоматически создает праймори ключ с автоинкрименцией
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY"
        for col, typ in columns.items():
            sql += f", {col} {typ}"
        sql += ")"
        self.cursor.execute(sql)
        self.conn.commit()
        print(f"Таблица {table_name} создана")

    def insert(self, table, data):
        cols = ', '.join(data.keys())
        vals = ', '.join([f"'{v}'" for v in data.values()])
        self.cursor.execute(f"INSERT INTO {table} ({cols}) VALUES ({vals})")
        self.conn.commit()
        print(f"запись добавлена в {table}")



    def get_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()


    def get_where(self, table, condition):
        """получить инфу по какому то параметру"""
        self.cursor.execute(f"SELECT * FROM {table} WHERE {condition}")
        return self.cursor.fetchall()



    def update(self, table, id, field, value):
        """Обновить поле у записи с указанным ID"""
        self.cursor.execute(f"UPDATE {table} SET {field} = '{value}' WHERE id = {id}")
        self.conn.commit()
        print(f"таблица {table} с айди={id} изменена")



    def delete_id(self, table, id):
        """Удалить запись по ид"""
        self.cursor.execute(f"DELETE FROM {table} WHERE id = {id}")
        self.conn.commit()
        print(f"таблица {table} с айди={id} удалена")

    def delete_where(self, table, condition):
        """Удалить записи по параметру"""
        self.cursor.execute(f"DELETE FROM {table} WHERE {condition}")
        self.conn.commit()
        print(f"таблица {table} с параментром  {condition} удалена")

    def drop(self,table):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table}")
        self.conn.commit()
        print(f"Таблица {table} полносью удалена")





    def close(self):

        self.conn.close()
        print("Соединение закрыто(так просили в документации pymysql)")


db = Database()
# пишите свой запрос

# db.create_table('python_auto',
#                 {'name': 'Varchar(255)',
#                  'lastname': 'Varchar(255)',
#                  'age': 'INT'
#                  })
db.drop('test69')


# после чего обязательо разорвать соединение
db.close()


