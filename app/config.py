from app.models.__pycache.news import News


class Config:
    '''
    General configuration parent class
    '''
    pass

   News _API_BASE_URL ='https://api.thenewsdb.org/3/news/{}?api_key={}'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True