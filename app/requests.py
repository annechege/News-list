# from app.main.views import article
import urllib.request,json
from .models import News, Article


# Getting api key
api_key = None
# Getting the movie base url
base_url = None
 #getting article url
article_url = None

def configure_request(app):
    global api_key,base_url,news_article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['ALL_NEWS_API_URL']
    news_article_url = app.config['ARTICLE_BASE_URL']



def get_news(category):
    """
  Function that gets the json response to our url request
  """
    get_news_url = base_url.format( category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_source = None
        if get_news_response["sources"]:
            news_source_list = get_news_response["sources"]
            news_source = process_source(news_source_list)
    return news_source


def process_source(news_list):
    """
    Function  that processes the news source and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_source: A list of news objects
    """
    news_source = []
    for news_item in news_list:
        id = news_item.get("id")
        name = news_item.get("name")
        description = news_item.get("description")
        url = news_item.get("url")
        category = news_item.get("category")
        country = news_item.get("country")
        news_object = News(
            id, name, description,url,category,country
        )
        news_source.append(news_object)
    return news_source


def process_article(news_list):
    """
    Function  that processes the news article and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_source: A list of news objects
    """
    news_article = []
    for news_item in news_list:
        id = news_item.get("id")
        author = news_item.get("author")
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")
        content = news_item.get("content")
        if urlToImage:
            news_object = Article(
                id, author,title,description,url,urlToImage,publishedAt,content
            )
            news_article.append(news_object)

    return Article


#Getting news article:
def get_article(id):
    """
  Function that gets the json response to our url request
  """
    get_news_url = news_article_url.format(id, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        article = None
        if get_news_response["articles"]:
            article_list = get_news_response["articles"]
            article = process_article(article_list)
    return article    