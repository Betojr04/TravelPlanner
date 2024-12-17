from models import db


class Trip(db.model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(
        db.String(100),
        nullable=False,
    )
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Float, nullable=False)

    activities = db.relationship("Activity", backref="trip", lazy=True)


class Activity(db.Model):
    __tablename__ = "activity"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(
        db.Integer,
        db.ForeignKey("trip.id"),
        nullable=False,
    )
    date = db.Column(db.Date, nullable=False)
    activity_name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
