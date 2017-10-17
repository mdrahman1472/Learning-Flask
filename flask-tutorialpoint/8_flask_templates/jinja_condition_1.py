from flask import Flask, render_template
app=Flask(__name__)

@app.route('/jinja_condition_1/<int:score>')
def score_check(score):
	return render_template('jinja_condition_1.html', marks=score)

if __name__ == '__main__':
	app.run(debug=True)