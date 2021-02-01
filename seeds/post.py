from flask_seeder import Seeder
from faker import Faker
from app.models import User, Post
from random import choice

en_fake = Faker('en_US')
ja_fake = Faker('ja_JP')


class PostSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 3

    def run(self):
        users = User.query.all()
        population = len(users)
        total = population * 20
        for num in range(1, population * 14):
            if num % 100 == 0:
                print(f"Adding post: {num} of {total}")
            post = Post(body=en_fake.text(max_nb_chars=140),
                        language='en',
                        timestamp=en_fake.past_datetime(start_date='-60d'),
                        user_id=choice(users).id)
            self.db.session.add(post)
        for num in range(population * 14, population * 20):
            if num % 100 == 0:
                print(f"Adding post: {num} of {total}")
            post = Post(body=ja_fake.text(max_nb_chars=140),
                        language='ja',
                        timestamp=ja_fake.past_datetime(start_date='-60d'),
                        user_id=choice(users).id)
            self.db.session.add(post)
