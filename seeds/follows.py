from flask_seeder import Seeder
from app.models import User
from random import randint, sample


class FollowSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 4

    def run(self):
        users = User.query.all()
        population = len(users)
        i = 0
        for root_user in users:
            others = sample([user for user in users if user.id is not root_user.id], randint(3, population // 2))
            for other_user in others:
                root_user.follow(other_user)
                i += 1
                if i % population == 0:
                    print(f"{root_user.username} is now following {other_user.username}!")