import os

class Config():
    LIMIT = 10
    TIME_LIMIT = 300 

class ProductionConfig(Config):
    REDIS_URL = os.environ.get('REDIS_URL')

class DevelopmentConfig(Config):
    LIMIT = 3
    TIME_LIMIT = 15 
    REDIS_URL = 'redis://localhost:6379'
