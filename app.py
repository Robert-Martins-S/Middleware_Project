from flask import Flask
from middleware import RequestTimingMiddleware

app = Flask(__name__)
app.wsgi_app = RequestTimingMiddleware(app.wsgi_app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/slow')
def slow():
    time.sleep(2)
    return "This was slow!"

if __name__ == '__main__':
    app.run(debug=True)
