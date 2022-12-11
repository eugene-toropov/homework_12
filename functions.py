import json
import logging
from json import JSONDecodeError


def get_data_from_json():
    try:
        with open("posts.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"


def search_post(word):
    posts = get_data_from_json()
    posts_with_word = []
    for post in posts:
        if word.lower() in post['content'].lower():
            posts_with_word.append(post)
    return posts_with_word


def save_pic(picture):
    try:
        filename = picture.filename
        filetype = filename.split('.')[-1]
        if filetype not in ['jpeg', 'jpg', 'png', 'bmp']:
            return

        picture.save(f"./uploads/{filename}")
        return f'uploads/{filename}'

    except:
        logging.error("Ошибка загрузки файла")
        return


def add_post_to_json(posts):
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file)


def add_post(post):
    posts = get_data_from_json()
    posts.append(post)
    if not add_post_to_json(posts):
        logging.error()
        return





print(get_data_from_json())
