import re
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__, template_folder='.')


@app.route("/")
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_time=current_time)


