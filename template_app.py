from flask import Flask, render_template  # フラスク最初の部分の雛形を用意してくれてる

app = Flask(__name__)


@app.route("/")
def index():
    # index.htmlをレンダリングする
    return render_template("index.html")


@app.route("/user/<name>")  # name関数に渡す
def hello(name):
    # index.htmlをレンダリングする
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
