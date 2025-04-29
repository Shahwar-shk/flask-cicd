# app.py
from flask import Flask, render_template
from views import main_blueprint  # Import the blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)

@app.route('/')
def home():
    return render_template('index.html', name="Flask App")

if __name__ == "__main__":
    app.run(debug=True)

