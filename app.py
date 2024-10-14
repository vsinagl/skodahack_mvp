from flask import Flask, render_template, Blueprint
from companies import InsuranceCompany
import yaml



def create_companies():
	# here but database retrieval code
	data = None
	companies = []
	with open('templates/companies/companies.yaml') as file:
		data = yaml.safe_load(file)
	for elem in data:
		company = InsuranceCompany(elem)
		companies.append(company)
	return companies
	
	


views = Blueprint("views", "home")
companies = create_companies()
# HARD coded active insurance company
active_insurance_company = companies[0]
print("THE PRICE IS: ",companies[0].price)

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/insurance")
def insurance():
	return render_template("insurance.html", user_insurance = active_insurance_company,
						companies = companies)


# app itself
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/", name="views")

if __name__ == "__main__":
	app.run(debug=True)
