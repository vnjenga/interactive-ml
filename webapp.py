from flask import Flask, render_template, request, redirect,url_for
from forms import SearchForm
import requests
import json
import unicodedata

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

@app.route('/', methods=['GET', 'POST'])
def home():
	form = SearchForm()
	if form.validate_on_submit():
		print('YAYYY')
		redirect_url = url_for('text', book=form.book.data, seed=form.seed.data)
		return redirect(redirect_ur)
	print(form.errors)
	return render_template('search.html', form=form)
	

@app.route('/text')
def text(book,seed):
	#r = request.args
	#api_url = 'http://localhost:8080/generate-text?book='+r['book']+'&seed='+r['seed']
	api_url = 'http://localhost:8080/generate-text?book='+book+'&seed='+seed
	info = requests.get(api_url)
	info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
	info = json.loads(info)
	return render_template('show.html', info=info)


if __name__ == '__main__':
	app.run(debug=True)