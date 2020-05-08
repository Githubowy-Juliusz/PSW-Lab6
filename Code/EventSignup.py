from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
Base = declarative_base()

class EventSignup(Base):
	__tablename__ = 'event_signup'
	id = Column(Integer, primary_key = True)
	id_user = Column(Integer)
	id_event = Column(Integer)
	participation_type = Column(String)
	catering = Column(String)
	accepted = Column(Boolean)
	def __init__(self, id, id_user, id_event, participation_type, catering, accepted):
		self.id = id
		self.id_user = id_user
		self.id_event = id_event
		self.participation_type = participation_type
		self.catering = catering
		self.accepted = accepted