from flask import Blueprint, render_template, request
from functions import search_post
import logging

mainpage_blueprint = Blueprint('mainpage_blueprint', __name__, template_folder='templates')
logging.basicConfig(handlers=[logging.FileHandler(filename='basic.log',encoding='utf-8', mode='a+')], level=logging.INFO)

@mainpage_blueprint.route('/')
def main_page():
    return render_template('index.html')


@mainpage_blueprint.route('/search')
def search_page():
    substr = request.args.get('s', '')
    logging.info(f'Поиск: {substr}')
    posts = search_post(substr)
    return render_template('post_list.html', posts=posts, substr=substr)

