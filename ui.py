from flask import Flask, render_template, request

app = Flask(__name__)


# Get nav
def get_navigation():
    return render_template("navigation.html")


# Define a simple route
@app.route('/')
def index():
    return render_template('home.html', navigation=get_navigation())


if __name__ == '__main__':
    app.run(debug=True)
