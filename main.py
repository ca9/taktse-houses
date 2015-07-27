from flask import Flask
 
app = Flask(__name__)

app.config['DEBUG'] = True

from flask import render_template
from datetime import datetime

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template("index.html", template_folder = "templates",  static_url_path='/static')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hellopage(name="from Taktse"):
 #  time_variable = datetime.now()
 #   return render_template('index.html', name=name, time=time_variable)
