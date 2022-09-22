from flask import Flask

# blueprint import
from forum.views import forum

# blueprint import

app = Flask(__name__)

# setup with the configuration provided
app.config.from_object('config.DevelopmentConfig')

# setup all our dependencies

# register blueprint
app.register_blueprint(forum)

if __name__ == '__main__':
    app.run()
