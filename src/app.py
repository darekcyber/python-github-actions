from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Siema"


if __name__ == "__main__":
    app.run()

print(__name__)