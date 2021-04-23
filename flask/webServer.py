
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"            #로컬 호스트 창 안에 출력되는 내용


if __name__ == "__main__":
    app.run(host = "localhost")       #로컬 호스트 창 열기
    