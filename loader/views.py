from flask import Blueprint, render_template, request
from functions import save_pic, add_post
import logging

loader_blueprint = Blueprint('loader_blueprint',__name__,template_folder='templates')
logging.basicConfig(handlers=[logging.FileHandler(filename='basic.log',encoding='utf-8', mode='a+')], level=logging.INFO)

@loader_blueprint.route("/post")
def create_new_post():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def post_upload():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        return "Данные не получены"

    try:
        picture_path = save_pic(picture)
    except:
        if not picture_path:
            logging.info(f'Файл {picture.filename} - не картинка')
            return "Файл - не картинка"

    new_post = {'pic': picture_path, 'content': content}
    add_post(new_post)

    return render_template("post_uploaded.html", picture_path=picture_path, content=content)



