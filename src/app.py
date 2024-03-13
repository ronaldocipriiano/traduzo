from os import environ
from flask import Flask
from waitress import serve
from controllers.admin_controller import admin_controller
from controllers.translate_controller import bp as translate_controller


app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")
app.register_blueprint(translate_controller, url_prefix="/")


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
