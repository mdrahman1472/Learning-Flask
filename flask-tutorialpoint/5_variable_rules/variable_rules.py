from flask import Flask 

app = Flask(__name__)

# <name> is variable name, it passed as keyboard
# argument to the function
@app.route('/hello/<name>')

def hello_name(name):
	return 'Hello %s!' %name



'''
Inaddition to string default variable, rules can be constructed
using int, float, and 
path(accepts slashes used as directory separator character)
'''

# using int 
@app.route('/blog/<int:postID>')
def show_blog(postID):
	return 'Blog Number %d' %postID

#using float
@app.route('/rev/<float:revNo>')
def revision(revNo):
	return 'Revision Number %f' %revNo


if __name__ == '__main__':
	app.run(debug=True)