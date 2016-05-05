from flask import Flask, render_template

import controllers
import os

# Construct a Flask app instance
app = Flask(__name__, template_folder='templates')

app.secret_key = "mW\xba\xed>C\xb3N8'\x1eC\xe7\xd7\xa0i\x02\x1e,\xf0|\xb4\xc8b"

# Register Controllers file
app.register_blueprint(controllers.index)

# Start server
if __name__ == '__main__':
	app.secret_key = "mW\xba\xed>C\xb3N8'\x1eC\xe7\xd7\xa0i\x02\x1e,\xf0|\xb4\xc8b"
	app.run(host='0.0.0.0', port=3000, debug=True)
