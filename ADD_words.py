import postgesql
import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="1111",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)




class BotDB:

    def __init__(self, db_file):
        self.conn = postgesql.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):   # Проверяем, есть ли юзер в базе

        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):  # Достаем word по  word_id

        result = self.cursor.execute("SELECT `id` FROM `words` WHERE `word_id` = ?", (word_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):  #  Добавляем слова в базу

        self.cursor.execute("INSERT INTO `words` (`word_id`) VALUES (?)", (word_id,))
        return self.conn.commit()


    def close(self):  #  Закрываем соединение с БД

        self.connection.close()
