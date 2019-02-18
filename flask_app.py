from flask import Flask, render_template, request
import main


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("domain")
    tupl = main.friends_finder(name)
    main.map_creator(tupl)
    return render_template("films.html")


if __name__ == "__main__":
    app.run(debug=True)