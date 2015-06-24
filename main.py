from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello World! \
	<br \> This is Aditya checking in. \
	<br  \> this is bibhu. \
	<br \> this is Abhishek Subba. \
	<br \> a piece of land surrounded by water on all four sides. \
	<br \> just for test - subbaman. \
	<br \> Amit checking in."


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
