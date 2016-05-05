from flask import *

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/')
def main_route():
	return render_template("graphs.html")	
