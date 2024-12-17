from flask import Blueprint


from routes.trip_routes import trip_routes


def register_blueprints(app):
    app.register_blueprint(trip_routes)
