import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABSE_URI = (
        f"sqlite:///{os.path.join(BASE_DIR, 'db/travel_planner.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
