import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "1"
db_name = "task1"

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    cursor = connection.cursor()

    # Создание таблицы PhoneBook
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    print("Таблица создана или уже существует")

    # Функция добавления через консоль
    def insert_from_console():
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        try:
            cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
            print("Данные успешно добавлены.")
        except Exception as e:
            print("Ошибка при добавлении данных:", e)

    # Функция обновления данных
    def update_data():
        field = input("Что вы хотите обновить? (name/phone): ").strip().lower()
        target = input("Введите текущее значение (имя или телефон): ").strip()
        new_value = input("Введите новое значение: ").strip()

        if field == "name":
            cursor.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_value, target))
        elif field == "phone":
            cursor.execute("UPDATE PhoneBook SET phone = %s WHERE phone = %s", (new_value, target))
        else:
            print("Неверное поле.")
            return
        print("Данные успешно обновлены.")



    # Функция запроса данных
    def query_data():
        print("Выберите фильтр:\n1 - все записи\n2 - По имени\n3 - По номеру\n4 - по промежутку id\n5 - по паттерну")
        choice = input("Введите номер выбора: ")

        if choice == "1":
            cursor.execute("SELECT * FROM PhoneBook ORDER BY id")
        elif choice == "2":
            name = input("Введите имя: ")
            cursor.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
        elif choice == "3":
            phone = input("Введите номер телефона: ")
            cursor.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
        elif choice == "4":
            id_start= input("Введите начало id: ")
            id_end= input("Введите конец id: ")

            cursor.execute("SELECT * FROM PhoneBook WHERE id >= %s AND id <= %s", (id_start, id_end))
        elif choice == "5":
                pattern = input("Write pattern: ")
                cursor.execute("SELECT * FROM PhoneBook WHERE name LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}%"))
    

            
            
        else:
            print("Неверный выбор.")
            return

        results = cursor.fetchall()
        for row in results:
            print(row)

    def query_with_pagination():
        try:
            limit = 5
            page = int(input("Номер страницы: "))

            offset = (page - 1) * limit
            cursor.execute("SELECT * FROM PhoneBook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
            results = cursor.fetchall()

            if results:
                print(f"\nРезультаты (страница {page}):")
                for row in results:
                    print(row)
            else:
                print("Нет данных на этой странице.")
        except Exception as e:
            print("Ошибка при запросе с пагинацией:", e)

    

    # Функция удаления
    def delete_data():
        print("Удалить по:\n1 - Имени\n2 - Телефону")
        choice = input("Введите номер выбора: ")

        if choice == "1":
            name = input("Введите имя: ")
            cursor.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
        elif choice == "2":
            phone = input("Введите номер телефона: ")
            cursor.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
        else:
            print("Неверный выбор.")
            return

        print("   Данные удалены.")
        # Сбросить последовательность для ID, чтобы следующий ID был правильным
        cursor.execute("SELECT setval(pg_get_serial_sequence('PhoneBook', 'id'), MAX(id)) FROM PhoneBook;")
        1
        print("    Данные удалены. ID пересчитаны.")

    def reset_table():
        confirm = input("    Это удалит все данные. Продолжить? (yes/no): ").lower()
        if confirm == "yes":
            try:
                cursor.execute("DROP TABLE IF EXISTS PhoneBook;")
                cursor.execute("""
                    CREATE TABLE PhoneBook (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        phone VARCHAR(20) NOT NULL
                    );
                """)
                print("   Таблица сброшена и создана заново.")
            except Exception as e:
                print("   Ошибка:", e)
        else:
            print("   Отменено.")

        
    def insert_many_users():
        lst_user = []
        lst_number = []
        size = int(input("number of users: "))
        print("\n")

        for i in range(size):
            user = input(f"Name of {i+1} user: ")
            number = input(f"Number of{user}: ")
            lst_user.append(user)
            lst_number.append(number)

        
        for i in range(size):
            try:
                cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (lst_user[i], lst_number[i]))
                print(f"User {lst_user[i]} is inserted to database")

            except Exception as e:
                print(f"Error of user{lst_user[i]}, {e}")



        
        
        
        



    # Простой интерфейс
    while True:
        print("\n   Меню PhoneBook:")
        print("1. Добавить запись")
        print("2. Добвить много записей")
        print("3. Обновить запись")
        print("4. Посмотреть записи")
        print("5. Удалить запись")
        print("6. Сбросить таблицу (удалить всё)")
        print("7. Выйти")
        print("8. Вывод пагинацией")

        option = input("Выберите действие: ")

        if option == "1":
            insert_from_console()
        elif option == "2":
            insert_many_users()
        elif option == "3":
            update_data()
        elif option == "4":
            query_data()
        elif option == "5":
            delete_data()
        elif option == "6":
            reset_table()
        elif option == "7":
            break
        elif option == "8":
            query_with_pagination()
        else:
            print("   Неверный ввод.")

except Exception as e:
    print("   Ошибка подключения к БД:", e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("   Соединение закрыто.")
