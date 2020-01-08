import flask

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_templates('main.html'))
	
	if __name__ == '__main__':
    app.run()