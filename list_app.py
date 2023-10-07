from flask import Flask, render_template

app = Flask(__name__)


@app.route("/members")
def members():
    # リストの作成
    members = ["Bob", "Tom", "Ken"]
    # 変数membersを渡してあげる
    return render_template("members.html", members=members)  # menbersHTMLを別ファイルで作るぜ


if __name__ == '__main__':
    app.run(port=8000, debug=True)