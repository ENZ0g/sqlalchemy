import sqlalchemy as a
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import null

from datetime import datetime as d


Base = declarative_base()


class Athletes(Base):
    __tablename__ = 'athelete'

    id = a.Column(
        a.Integer,
        primary_key=True,
        autoincrement=True,
    )
    age = a.Column(a.Integer)
    birthdate = a.Column(a.Text)
    gender = a.Column(a.Text)
    height = a.Column(a.Float)
    name = a.Column(a.Text)
    weight = a.Column(a.Integer)
    gold_medals = a.Column(a.Integer)
    silver_medals = a.Column(a.Integer)
    bronze_medals = a.Column(a.Integer)
    total_medals = a.Column(a.Integer)
    sport = a.Column(a.Text)
    country = a.Column(a.Text)


def find_nearest_height(height, session):
    query = session.query(Athletes.height, Athletes.name).\
        filter(Athletes.height != null()).\
        order_by(Athletes.height.desc())
    max_delta = query[0].height - height
    delta = [(abs(i.height - height), i.name, i.height) for i in query if abs(i.height - height) <= max_delta]
    delta.sort(key=lambda x: x[0])
    print('\n', '=' * 20, sep='')
    print('Ближайший рост:', '\n')
    print(f'{delta[0][1]} -- {delta[0][2]}')
    print('=' * 20, '\n')


def find_nearest_bdate(date, session):
    query = session.query(Athletes.birthdate, Athletes.name).\
        order_by(Athletes.birthdate)
    date = d.strptime(date, '%d.%m.%Y')
    days_delta = [(abs((d.strptime(i.birthdate, '%Y-%m-%d') - date).days), i.name, i.birthdate) for i in query]
    days_delta.sort(key=lambda x: x[0])
    print('\n', '=' * 20, sep='')
    print('Ближайший день рождения:', '\n')
    print(f'{days_delta[0][1]} -- {days_delta[0][2]}')
    print('=' * 20, '\n')
