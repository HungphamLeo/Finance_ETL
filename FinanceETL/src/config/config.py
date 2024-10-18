
class Config:
    LOGGER_PATH = './logger/'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'YOUR DB PASSWORD'
    MYSQL_DATABASE = 'YOUR DB NAME'
    DATABASE_NAME = 'YOUR DB NAME'

    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB_URL = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/'
