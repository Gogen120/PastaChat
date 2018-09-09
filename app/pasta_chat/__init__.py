from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/postgres'.format('postgres', 'pasta', 'pasta_chat.postgres', '5432')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
