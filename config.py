import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-super-secret-key'
    SQL_ALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
