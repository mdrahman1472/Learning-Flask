from flask import Flask 

app = Flask(__name__)

# <name> is variable name, it passed as keyboard
# argument to the function
@app.route('/hello/<name>')

def hello_name(name):
	return 'Hello %s!' %name

if __name__ == '__main__':
	app.run(debug=True)

