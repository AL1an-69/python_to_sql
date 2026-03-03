## Как использовать:
```python
from database import db

# создать таблицу
db.create_table('users', {'name': 'VARCHAR(100)', 'age': 'INT'})

# добавить 
db.insert('users', {'name': 'Иван', 'age': 20})

# посмотреть всех
print(db.get_all('users'))

# закрыть обязательно
db.close()