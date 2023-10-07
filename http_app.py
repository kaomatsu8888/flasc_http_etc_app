from flask import Flask, request

app = Flask(__name__)


# Getだったらこの処理 POSTだったらこの処理というふうにしていく
# ログイン機能 $ curl http://127.0.0.1:8000/login bash上で動かすコマンド データ送る場合$ ＄ curl -X POST $ curl http://127.0.0.1:8000/login
@app.route("/login", methods=["GET", "POST"])  # Getかpostだったときにメソッド動きますよ！
def login():
# デバッグモード デバックコンソールで見て、request.methodを入れる request.url request.headers ポスト表示
# リクエストメソッドGETのときは以下の処理を行う
    if request.method == "GET":
        return '''
        <form action="/login" method="post">
        Password:<input type="text"><br>
        <input type='submit'>
        </from>
        '''
# リクエストメソッドPOSTの時は以下の処理を行う
    return "Logged in" #getじゃなかった時この処理する


if __name__ == "__main__":
    app.run(port=8000, debug=True)  # デバッグトゥルーを後で要確認  #コントロールシー 右下Python内(bashじゃない)でサーバー止める→↓分割表示できる
