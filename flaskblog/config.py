import os
import psycopg2

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')  #'a99c515275ef1355c18ff3efc46221ce'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  #'sqlite:///site.db'
	conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI, sslmode='require')
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')