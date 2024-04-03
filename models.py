#crud/models.py
from sqlalchemy import Column, Integer, String
from database import Base
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    position = Column(String(150))
    office = Column(String(150))
 
    def __repr__(self):
        return '<User %r>' % (self.id)