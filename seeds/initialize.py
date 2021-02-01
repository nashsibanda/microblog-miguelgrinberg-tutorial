from flask_seeder import Seeder
from app.models import User, Post

class UserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    def run(self):
        users = self.db.session.query(User).delete()
        print("%d users deleted." % users)
        posts = self.db.session.query(Post).delete()
        print("%d posts deleted." % posts)