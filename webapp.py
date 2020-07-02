from flask import Flask, render_template, request, redirect,url_for
from forms import SearchForm
import requests
import json
import unicodedata
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def home():
	form = SearchForm()
	if form.validate_on_submit():
		redirect_url = url_for('text', book=form.book.data, seed=form.seed.data)
		return redirect(redirect_url)
	#print(form.errors)
	return render_template('search.html', form=form)
	

@app.route('/text')
def text():
	r = request.args
	api_url = 'http://localhost:8080/generate-text?book='+r['book']+'&seed='+r['seed']
	#api_url = 'http://localhost:8080/generate-text?book='+book+'&seed='+seed
	print('Got url:',api_url)
	info = requests.get(api_url)
	info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
	info = json.loads(info)
	return render_template('show.html', info=info)


if __name__ == '__main__':
	app.run(debug=True)