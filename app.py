from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'fa'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

# Function to get the current locale
def get_locale():
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Initialize Babel
babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)
