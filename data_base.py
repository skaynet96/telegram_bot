import sqlite3

base = sqlite3.connect('new.db')  # base - это экземпляр класса connection, создаем файл базы данных, файл "new.db"
cur = base.cursor()   # cur будет записывать и читать данные из БД

base.execute('CREATE TABLE IF NOT EXISTS {}(продукты PRIMARY KEY)'.format('data')) # PRIMARY KEY - фильтрует столбец "login" чтобы были уник.значения
#base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
# создаем таблицу, data - название таблицы, "login" и "password" - создаем столбцы в табле
# IF NOT EXIST - прописываем, чтобы при повторном запуске не было ошибки "table data already exists"

base.commit() # эта штука сохраняет изменения в таблице

# #cur.execute('INSERT INTO data VALUES(?, ?)', ("jonny123", "123456789"))  # Пишем так, чтобы избежать такого хакинга, как "SQL инъекция"
# base.commit()
# cur.execute('INSERT INTO data VALUES(?, ?)', ('billy123', "password"))
# base.commit()


#r = cur.execute('SELECT * FROM data').fetchall()
# * - обозначает, что мы получаем все значения из этой таблицы
# SELECT - мы получаем данные из БД
# fetchall - получить все значения
#print(r)

#r = cur.execute('SELECT login FROM data').fetchall()
#print(r)
# прописав "login" после SELECT , мы обратимся только к столбцу "login"


#r = cur.execute('SELECT password FROM data WHERE login == ?', ("jonny123",)).fetchone()
#print(r)
# выбрать значение из data где login == jonny123
# fetchone - используем метод, чтобы получить одно значение

# cur.execute('UPDATE data SET password == ? WHERE login == ?', ('12345678', 'jonny123'))
# base.commit()
# # изменить значение ячейки в столбце password


#cur.execute('UPDATE data SET password == ? WHERE password == ?', ('12345678', 'password'))
#base.commit()
#множественная замена в поле password строк с значением password
#скрипт находит все строки с значением password и меняет на 123456789

#cur.execute('DELETE FROM data WHERE login == ?', ('jonny123', ))
#base.commit()
# удаление ячейки
# , ('jonny123', )) - этот участок кода называется кортеж


#base.execute(('DROP TABLE IF EXISTS data'))
#base.commit()
# этот код удаляет всю таблицу

#base.close()
# эту команду обязательно оставляем в конце кода, чтобы безопасно закончить работу с базой данных


#text, integer, real, blob, null #5 типов данных в SQLite
# real - число с плавающей точкой
# blob - в этом столбце может быть любой тип данных
# null - тип данных none
# особого смысла в этом нет, так как проконтролировать типы данных тяжело

