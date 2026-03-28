import pymysql
from app.config import DB_CONFIG
import csv



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

    ################################
    
    """новые запросы для лр_1"""


    def col_desc(self,table,colum):
        self.cursor.execute(f"SELECT {colum} FROM {table} ORDER BY {colum} DESC")
        self.conn.commit()
        print(f"Таблица {table} отсартирована убывающе по столбцу {colum} ")
    
    def id_range_select(self,table,start_id,end_id):
        self.cursor.execute(f"SELECT * FROM {table} WHERE BERWEN {start_id} AND {end_id}")
        self.conn.commit()
        print(f"Выведены все значения из талицы {table} в диапазоне айди от {start_id} до {end_id}")

    def id_range_delete(self,table,start_id,end_id):
        self.cursor.execute(f"DELETE * FROM {table} WHERE BERWEN {start_id} AND {end_id}")
        self.conn.commit()
        print(f"Удалены все значения из талицы {table} в диапазоне айди от {start_id} до {end_id}") 
    
    def table_info(self,table):
        self.cursor.execute(f"DISCRIBE {table}")
        return self.cursor.fetchall()

    def find_value(self,table,colum,value)
        self.cursor.execute(f"SELECT * FROM {table} WHERE {column} = {value}")
        print(f"Выведены все столбцы {colum} со значением {value}")
        
    def add_colum(self,table,colum,typ):
        self.cursor.execute(f"ALTER TABLE {table} ADD {colum} {typ}")
        self.conn.commit()
        print(f"В таблицу {table} добавлен столбец {colum} с типом {typ}")
    
    def del_colum(self,table,colum):
        self.cursor.execute(f"ALTER TABLE {table} DROP {colum}")
        self.conn.commit()
        print(f"Из таблицы {table} удален столбец {colum}")

    def export_csv(self,table,file_name):
        self.cursor.execute(f"SELECT * FROM {table}")
        rows = self.cursor.fetchall()
        with open(file_name, 'w') as f:
            for row in rows:
                f.write(','.join(str(x) for x in row) + '\n')
        print(f"Таблица {table} экспортирована в файл {file_name}")

    def import_csv(self,table,file_name):
        with open(file_name, 'r') as f:
            for line in f:
                values = line.strip().split(',')
                self.insert(table, dict(zip(self.table_info(table), values)))
        print(f"Данные из файла {file_name} импортированы в таблицу {table}")
  










