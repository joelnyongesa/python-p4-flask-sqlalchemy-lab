from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)

    # Insert list of animals
    animals = db.relationship('Animal', backref='zookeeper')

    def __repr__(self):
        return f"<Zookeeper {self.id}, name {self.name} and birthday {self.birthday} animals: {self.animals}>"


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    # List of animals
    animals = db.relationship('Animal', backref="enclosure")

    def __repr__(self):
        return f"Enclosure {self.id} and Environment {self.environment}\
            Open to visitors: {self.open_to_visitors}\
            Animals: {self.animals}"

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    # Zoo keeper and enclosure
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    def __repr__(self):
        return f'<Animal  {self.name} of species {self.species}'
