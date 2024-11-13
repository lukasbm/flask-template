from app import db


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column('ID', db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column('Name', db.String(64), nullable=True)
    
    def __repr__(self):
        return f'<Share {self.name}>'
