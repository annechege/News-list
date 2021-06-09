from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_article, get_news
#views
@main.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    title = "Home || News Sources"
    all_news = get_news('sports')
    general_news = get_news('general')
    tech_news = get_news('technology')
    bus_news = get_news('business')
    sci_news = get_news('science')
    return render_template('index.html', title= title, sports = all_news, general = general_news, technology = tech_news, business = bus_news, science = sci_news)
# Views
@main.route('/news/<int:id>')
def news(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)
    return render_template('index.html', news = news)
@main.route('/article/<source_id>')
def article(source_id):
    '''
    function that returns articles by source id
    '''
    articles= get_article(source_id)
    title = f'{source_id}| Article'
    return render_template('article.html',title = title, name = source_id, articles = articles )
