import mysql.connector as mysql
import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Date, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from User import User
from EventSignup import EventSignup
from Event import Event

class DB:
	def __init__(self):
		self.host = "127.0.0.1"
		self.user = "root"
		self.password = "githubowyjuliusz"
		self.schema = "pswdb"
		self.engine = create_engine(f"mysql://{self.user}:{self.password}@{self.host}/{self.schema}", echo=True)
		self.meta_data = MetaData(self.engine)
		self.session = sessionmaker(bind=self.engine)()

	def get_users_table(self):
		query_result = self.session.query(User.id, User.name, User.last_name, User.login, User.password, User.email, User.permission, User.registration_date)
		users = query_result.all()
		return users
	
	def get_events_table(self):
		query_result = self.session.query(Event.id, Event.name, Event.agenda, Event.date)
		events = query_result.all()
		return events

	def get_pending_signups(self):
		query_result = self.session.query(EventSignup.id, EventSignup.id_user, EventSignup.id_event, EventSignup.participation_type, EventSignup.catering, EventSignup.accepted).filter(EventSignup.accepted == False)
		event_signups = query_result.all()
		return event_signups

	def get_event_names(self):
		query_result = self.session.query(Event.name)
		events = query_result.all()
		return events
	
	def get_event_details(self, event_name):
		query_result = self.session.query(Event.id, Event.name, Event.agenda, Event.date).filter(Event.name == event_name)
		events = query_result.all()
		return events
	
	def insert_user(self, user):
		self.session.add(user)
		self.session.commit()
	
	def insert_event(self, event):
		self.session.add(event)
		self.session.commit()
	
	def insert_event_signup(self, event_signup):
		self.session.add(event_signup)
		self.session.commit()
	
	def delete_user(self, id):
		self.session.query(User).filter(User.id == id).delete()
		self.session.commit()

	def delete_event(self, id):
		self.session.query(Event).filter(Event.id == id).delete()
		self.session.commit()
	
	def delete_signup(self, id):
		self.session.query(EventSignup).filter(EventSignup.id == id).delete()
		self.session.commit()
	
	def accept_signup(self, id):
		query_result = self.session.query(EventSignup).filter(EventSignup.id == id)
		event_signup_list = query_result.all()
		event_signup = event_signup_list[0]
		event_signup.accepted = True
		self.session.commit()
	
	def change_users_password(self, id, password):
		query_result = self.session.query(User).filter(User.id == id)
		user_list = query_result.all()
		user = user_list[0]
		user.password = password
		self.session.commit()
	
	def update_event(self, event):
		query_result = self.session.query(Event).filter(Event.id == event.id)
		event_list = query_result.all()
		selected_event = event_list[0]
		selected_event.name = event.name
		selected_event.agenda = event.agenda
		selected_event.date = event.date
		self.session.commit()
	
	def check_if_already_signed_up(self, event_signup):
		query_result = self.session.query(EventSignup).filter(EventSignup.id_user == event_signup.id_user, EventSignup.id_event == event_signup.id_event)
		event_signup_list = query_result.all()
		if event_signup_list == []:
			return False
		return True
	
	def check_login_and_password(self, login, password):
		query_result = self.session.query(User).filter(User.login == login, User.password == password)
		table = query_result.all()
		return table
	
	def is_login_taken(self, user):
		query_result = self.session.query(User).filter(User.login == user.login)
		users_list = query_result.all()
		if users_list == []:
			return False
		return True