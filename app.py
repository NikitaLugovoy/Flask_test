from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1> Здравствуй flask </h1> <p>Вторая сторочка </p>"\
           "<table border='1px solid black' > <tr><th>Путин</th> <th>Владимир</th></tr></table>"

@app.route('/hello')
def greeting():
    return "<h1> Привет Коля </h1> <p>Вторая сторочка </p>"\
           "<table border='1px solid black' > <tr><th>Путин</th> <th>Владимир</th></tr></table>"


if __name__ == '__main__':
    app.run(debug=True)
