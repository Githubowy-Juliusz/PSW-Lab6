from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
Base = declarative_base()

class Event(Base):
	__tablename__ = 'event'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	agenda = Column(String)
	date = Column(Date)
	def __init__(self, id, name, agenda, date):
		self.id = id
		self.name = name
		self.agenda = agenda
		self.date = date