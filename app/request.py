
from app.news_test import News
import urllib.request,json
from .models import news
News = news.News
# Getting api key
api_key = app.config['News_API_KEY']
# Getting the news base url
base_url = app.config["News_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)
    return news_results
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        vote_average = news_item.get('vote_average')
        vote_count = news_item.get('vote_count')
        movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
        movie_results.append(movie_object)
    return movie_results
def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)
        movie_object = None
    if movie_details_response:
       id = movie_details_response.get('id')
       title = movie_details_response.get('original_title')
       overview = movie_details_response.get('overview')
       poster = movie_details_response.get('poster_path')
       vote_average = movie_details_response.get('vote_average')
       vote_count = movie_details_response.get('vote_count')
       movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
       return movie_object
def search_movie(movie_name):
    search_movie_url ='https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)
        search_movie_results = None
        if search_movie_response['results']:
           search_movie_list = search_movie_response['results']
           search_movie_results = process_results(search_movie_list)
    return search_movie_results
