import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "instance", "site.db")

print(f"Database path: {db_path}")
print(f"Instance directory exists: {os.path.exists(os.path.join(basedir, 'instance'))}")
print(f"Instance directory writable: {os.access(os.path.join(basedir, 'instance'), os.W_OK)}")

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



