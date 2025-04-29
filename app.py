# app.py
from flask import Flask, render_template
from views import main_blueprint  # Import your blueprint if applicable

app = Flask(__name__)

# Register the blueprint (if you're using one)
app.register_blueprint(main_blueprint)

@app.route('/')
def home():
    return render_template('index.html')  # Render the 'index.html' file from the templates folder

if __name__ == '__main__':
    app.run(debug=True)


