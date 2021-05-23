from controller import profileController
from flask import make_response


def init_route(app):
    @app.route("/")
    @app.route("/api/v1/profileController/get_profiles", methods=['GET'])
    def get_profiles():
        return profileController.get_profiles()

    @app.route("/api/v1/profileController/get_profile", methods=['GET'])
    def get_profile():
        return profileController.get_profile()

    @app.route("/api/v1/profileController/insert_profile", methods=['POST'])
    def insert_profile():
        return profileController.insert_profile()
