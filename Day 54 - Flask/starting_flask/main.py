from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# this is how user input is rendered in the function by the url path
@app.route("/user/<string:name>/")
def user_greeting(name):
    return f"Why hello there {name}"


if __name__ == "__main__":
    app.run(debug=True)