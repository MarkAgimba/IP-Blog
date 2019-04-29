import os

class Config:
    '''
    General config parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mark:aguero10@localhost/blogapp'

    # email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde configs
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    UPLOADED_PHOTOS_DEST ='app/static/photos'