import os
class Config:
	SECRET_KEY = os.environ['SECRET_KEY']
	SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = 1
	MAIL_USERNAME = os.environ['DB_USER']
	MAIL_PASSWORD = os.environ['DB_PASS']
	
