import users
import find_athlete


DB_PATH = 'sqlite:///sochi_athletes.sqlite3'

session = users.db_connect(DB_PATH)

while True:
    choice = input('Выберете режим:\n'
                   '1. Добавить пользователя\n'
                   '2. Найти атлета с ближайшими к пользователю параметрами\n'
                   '3. Показать всех пользователей\n'
                   '4. Выйти\n>')

    if choice == '1':
        user = users.user_data_request()
        session.add(user)
        session.commit()
        print('\n', '=' * 21, sep='')
        print('Информация сохранена!')
        print('=' * 21, '\n')
    elif choice == '2':
        birhdate, height = users.get_user_from_db(session)
        if birhdate == 0 and height == 0:
            continue
        else:
            find_athlete.find_nearest_bdate(birhdate, session)
            find_athlete.find_nearest_height(height, session)
    elif choice == '3':
        users.get_all_users(session)
    elif choice == '4':
        break

