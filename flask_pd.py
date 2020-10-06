from flask import Flask
from flask import render_template, request
from flask_bootstrap import Bootstrap
import pandas as pd


app = Flask(__name__)
Bootstrap(app)

csv_file = '/root/menyparse/menu.csv'


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
        if request.form.get("TYPE1"):
            df = df.query('TYPE.str.contains("1")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE2"):
            df = df.query('TYPE.str.contains("2")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE3"):
            df = df.query('TYPE.str.contains("3")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE4"):
            df = df.query('TYPE.str.contains("4")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE5"):
            df = df.query('TYPE.str.contains("5")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE6"):
            df = df.query('TYPE.str.contains("Mexikanska")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE7"):
            df = df.query('TYPE.str.contains("Inbakade")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE8"):
            df = df.query('TYPE.str.contains("Halv")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE9"):
            df = df.query('TYPE.str.contains("Kebab")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("TYPE10"):
            df = df.query('TYPE.str.contains("Pepper")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("CONTENT1"):
            df = df.query('CONTENT.str.contains("ananas")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("CONTENT2"):
            df = df.query('CONTENT.str.contains("banan")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("CONTENT3"):
            df = df.query('CONTENT.str.contains("kyckling")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("CONTENT4"):
            df = df.query('CONTENT.str.contains("mozzarella")', engine='python')
            return render_template('pizza_pd.html', df=df.to_html())
        elif request.form.get("CONTENT5"):
            df = df.query('CONTENT.str.contains("parmaskinka")', engine='python')
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
