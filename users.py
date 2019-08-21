import sqlalchemy as a
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = a.Column(
        a.Integer,
        primary_key=True,
        autoincrement=True
    )
    first_name = a.Column(a.Text)
    last_name = a.Column(a.Text)
    gender = a.Column(a.Text)
    email = a.Column(a.Text)
    birthdate = a.Column(a.Text)
    height = a.Column(a.Float)


def db_connect(path):
    engine = a.create_engine(path)
    Base.metadata.create_all(engine)
    Sessions = sessionmaker(engine)
    return Sessions()


def user_data_request():
    print('Введите ваши данные!')
    name = input('Имя: ')
    last_name = input('Фамилия: ')
    sex = input('Пол (м/ж): ')
    while sex not in ['м', 'ж']:
        sex = input('Достаточно ввести "м" или "ж". Попробуйте снова: ')
    height = input('Рост в м (например 1.82): ').replace(',', '.')
    birth_date = input('Дата рождения (ДД.ММ.ГГГГ): ')
    email = input('E-mail: ')
    while is_valid_email(email):
        email = input('Некорректный адрес. Попробуйте снова: ')

    user = User(
        first_name=name,
        last_name=last_name,
        gender=sex,
        birthdate=birth_date.replace(',', '.').replace('-', '.').replace('/', '.'),
        email=email,
        height=height
    )

    return user


def is_valid_email(email):
    if email:
        if '@' in email:
            if '.' in email.split('@')[1]:
                return False
    return True


def get_user_from_db(session):
    name = input('Введите Ваше имя: ')
    query = session.query(User).filter(User.first_name == name)
    if query.count() == 0:
        print('\n', 'Пользователей с такими данными нет!', '\n')
        return 0, 0

    if query.count() > 1:
        last_name = input('В базе данных несколько пользователей с таким именем.\n'
                          'Введите фамилию: ')
        query = session.query(User).filter(User.first_name == name, User.last_name == last_name)

    birthdate, height = [(i.birthdate, i.height) for i in query][0]
    return birthdate, height
