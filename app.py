from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/about")
def about():
    return "<p>About, main</p>"

if __name__=="__main__":
    app.run(debug=True, port=5000)