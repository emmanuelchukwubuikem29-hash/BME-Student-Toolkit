from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/convert")
def convert():
    return render_template("convert.html", result=None, error=None)

@app.route("/tasks")
def tasks():
    return "Tasks page coming next."

if __name__ == "__main__":
    app.run(debug=True)