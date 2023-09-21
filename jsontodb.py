import json
from app.models import Post
from pprint import pprint
from app import db


def jsontodb(text):
    for sl in text:
        post = Post(car_brand=sl['car_brand'], color=sl['color'], model=sl['model'], \
                    year=sl['year'], price=sl['price'], engine=sl['engine'], transmission=sl['transmission'], \
                    power=sl['power'], location=sl['location'], mileage=sl['mileage'], description=sl['description'])
        db.session.add(post)
        db.session.commit()


with open('auto_desc.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    jsontodb(text)





