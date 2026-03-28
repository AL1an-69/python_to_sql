## Как использовать:
```python
from database import db

# создать таблицу
db.create_table('users', {'name': 'VARCHAR(100)', 'age': 'INT'})

# добавить 
db.insert('users', {'name': 'Иван', 'age': 20})

# посмотреть всех
print(db.get_all('users'))

# отсортировать по столбцу убывающе
# (например, отсортировать пользователей по возрасту)
db.col_desc('users', 'age')

# выбрать записи в диапазоне ID
db.id_range_select('users', 1, 10)

# удалить записи в диапазоне ID
db.id_range_delete('users', 1, 10)

# найти записи по значению в столбце
db.find_value('users', 'name', 'Иван')

# закрыть обязательно
db.close()
```