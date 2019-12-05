import sqlite3
from db import db

# extend db model, creating maps between models


class ItemModel(db.Model):
    __tablename__ = 'items'
    # Define db column
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    # find_by_name returns an object not a dict, but rest should return json
    # helper function to format the object data to json
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # sqlalchemy query builder, translate into sql
        # return item model object from row
        # object returned may need to be converted to json
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # convert object to row
        # session is a collection of objects that going to write into db
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
