import pymysql

# Параметры подключения к вашей базе данных
connection = pymysql.connect(host='hostname',
                             user='username',
                             password='password',
                             database='databasename',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Создание новой записи
        sql = "INSERT INTO `table_name` (`column1`, `column2`) VALUES (%s, %s)"
        cursor.execute(sql, ('value1', 'value2'))

    # Подтверждение вставки данных
    connection.commit()
