from flask import Flask, render_template, Blueprint


views = Blueprint("views", "home")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/insurance")
def insurance():
      return render_template("insurance.html")



# app itself
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/", name="views")

if __name__ == "__main__":
	app.run(debug=True)
