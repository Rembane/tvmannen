import os
curdir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "verysecretXd"
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(curdir, 'db.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(curdir, "static", "pr")
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4'}
    PR_TIME = 30        # Time for each PR in seconds
    PR_FETCH_TIME = 120 # How often the PR list is fetched
