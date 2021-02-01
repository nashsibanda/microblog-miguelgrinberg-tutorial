from flask_seeder import Seeder
from faker import Faker
from werkzeug.security import generate_password_hash
from app.models import User, Post
from random import randint

fake = Faker(['en_GB', 'ja_JP'])

class UserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 2

    def run(self):
        for num in range(1, 51):
            if num % 10 == 0:
                print("Adding user: %s" % num)
            user = User(username=fake.unique.user_name(),
                     email=fake.unique.safe_email(),
                     password_hash=generate_password_hash('testpass'),
                     about_me=fake.paragraph())
            self.db.session.add(user)
