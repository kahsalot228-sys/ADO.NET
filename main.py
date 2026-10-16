import mssql_python

# 3. Создайте соединение и строку подключения.
# ВАЖНО: Замените значения на свои данные.
# SERVER - имя вашего сервера (например, localhost\SQLEXPRESS или .\SQLEXPRESS)
# DATABASE - имя вашей базы данных
# UID/PWD - логин и пароль, если используется SQL-авторизация.
# Если у вас Windows Authentication (Trusted Connection), параметры UID/PWD не нужны.

connection_string = (
    "SERVER=localhost;" 
    "DATABASE=MyTestDB;" 
    "UID=sa;" 
    "PWD=YourStrongPassword123;"
    "TrustServerCertificate=yes;"
)

try:
    # Устанавливаем соединение
    print("Попытка подключения к базе данных...")
    conn = mssql_python.connect(connection_string)
    
    # 2. Создайте курсор из соединения
    cursor = conn.cursor()
    print("Соединение успешно установлено!")

    # Выполняем SELECT запрос
    # Предположим, у нас есть таблица Users с колонками Id и Name
    query = "SELECT Id, Name FROM Users" 
    
    # 4. Выполняем запрос (execute)
    cursor.execute(query)

    # 4. Результат выведите в консоль с помощью цикла for
    print("\nРезультат запроса:")
    print("-" * 20)
    
    # fetchall() получает все строки результата
    rows = cursor.fetchall()
    
    for row in rows:
        # row - это кортеж значений, например (1, 'Ivan')
        print(f"ID: {row[0]}, Name: {row[1]}")

    print("-" * 20)

except Exception as e:
    print("Ошибка при работе с базой данных:")
    print(e)

finally:
    # Закрываем соединение (хорошая практика)
    if 'conn' in locals() and conn:
        conn.close()
        print("Соединение закрыто.")