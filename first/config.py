import os

class Config:
    SECRET_KEY = 'd4c0cb813d664e0851a2ec6b1cc0c4a4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465

    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('DB_USER')
    MAIL_PASSWORD = os.environ.get('DB_PASSWORD')
