from flask import Flask

# blueprint import
from forum.views import forum

from google.cloud import ndb


app = Flask(__name__)

client = ndb.Client()


def ndb_wsgi_middleware(wsgi_app):
    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware


# setup with the configuration provided
app.config.from_object('config.DevelopmentConfig')

# setup all our dependencies
app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)

# register blueprint
app.register_blueprint(forum)

if __name__ == '__main__':
    app.run()
