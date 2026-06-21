from app import app

@app.route('/')
def home():
    return "<h1>Welcome to the Flaskassa!</h1>"