"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core Lightymon."""
    #app = Flask(__name__, instance_relative_config=False)
    app = Flask(__name__)
    #app.config.from_object("config.Config")
    #app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm"
    #app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}

    with app.app_context():
        # Import parts of Lightymon
        from . import routes

        return app
