from flask import Flask
from flask import render_template, request
from flask_bootstrap import Bootstrap
import pandas as pd


app = Flask(__name__)
Bootstrap(app)

csv_file = 'menu.csv'


@app.route("/list")
def show_tables():
	df = pd.read_csv(csv_file, sep='\t', header=0)
	df = df.groupby(by=['NUMBER', 'NAME', 'CONTENT', 'PRICE', 'TYPE']).sum()
	return render_template('pizza_pd.html', df=df.to_html())


@app.route("/ananas")
def show_ananas():
	df = pd.read_csv(csv_file, sep='\t', header=0)
	df = df.groupby(by=['NUMBER', 'NAME', 'CONTENT', 'PRICE', 'TYPE']).sum()
	df = df.query('CONTENT.str.contains("ananas")', engine='python')
	return render_template('pizza_pd_search.html', column_names=df.columns.values,
						   row_data=list(df.values.tolist()), link_column="NUMBER")

@app.route('/', methods=['GET', 'POST'])
def search():
	df = pd.read_csv(csv_file, sep='\t', header=0)
	df = df.groupby(by=['NUMBER', 'NAME', 'CONTENT', 'PRICE', 'TYPE']).sum()
	if request.method == "POST":
		if search_text := request.form.get('fritext'):
			print(f'Searching for: {search_text}')
			df = df.query(f'CONTENT.str.contains("{search_text}", case=False)', engine='python')
			return render_template('pizza_pd.html', df=df.to_html())
		elif pizza_type := request.form.get("type"):
			print(f'Selected pizza type: {pizza_type}')
			df = df.query(f'TYPE.str.contains("{pizza_type}", case=False)', engine='python')
			return render_template('pizza_pd.html', df=df.to_html())
		else:
			ingredient = request.form.get('ingredient')
			print(f'Listing with ingredient: {ingredient}')
			df = df.query(f'CONTENT.str.contains("{ingredient}", case=False)', engine='python')
			return render_template('pizza_pd.html', df=df.to_html())
	else:
		return render_template('search_pd.html', df=df.to_html)


@app.route('/cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
	df = pd.read_csv(csv_file, sep='\t', header=0)
	df = df.groupby(by=['NUMBER', 'NAME', 'CONTENT', 'PRICE', 'TYPE']).sum()
	product = df.query.filter('CONTENT' == product_id, engine='python')
	df.result = df.query.filter(product)
	print(df.result)


if __name__ == "__main__":
	app.run(debug=True)
