# _*_ coding:utf-8 _*_
from ._base import db

# dict = Person.__dict__
# dict.get('__table__')

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(10) ,unique=True)
    birth_date = db.Column(db.Date)

    def __repr__(self):
        return '<Person %s>' % self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'birthday': self.birth_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(20), unique=True)
    vendor = db.Column(db.Unicode(30))
    purchase_time = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    owner = db.relationship('Person', backref=db.backref('computers', lazy='dynamic'))

    def __repr__(self):
        return '<Computer %s>' % self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'vendor': self.vendor
        }
