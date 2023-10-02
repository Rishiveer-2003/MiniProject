from flask import Flask, render_template, request, redirect, url_for
import subprocess  # Import the subprocess module

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def getSearchTerm():
    flipkart_query = None

    if request.method == 'POST':
        if 'search_query' in request.form:
            flipkart_query = request.form['search_query'].strip()
            search_term = flipkart_query.replace(' ', '+')
            search_url = f'https://www.flipkart.com/search?q={search_term}'
            with open('templates/search_url.txt', 'w') as file:
                file.write(search_url)
            subprocess.call(['python', 'scraper2.py'])

        return redirect(url_for('showSearchList'))

    return render_template('home.hbs', flipkart_query=flipkart_query)

@app.route('/search_list')
def showSearchList():
    return render_template('search_list.html')

if __name__ == '__main__':
    app.run(debug=True)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

