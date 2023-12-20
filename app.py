from cs50 import SQL
from flask import Flask, render_template, request, send_file
from word_frequency import WordFrequency

app = Flask(__name__)

db = SQL("sqlite:///frequency.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        text = request.form.get("text")

        if not text:
            return render_template("error.html", message="Enter Some Text")
        if len(text) < 100:
            return render_template("error.html", message="Minimum text length should be 100 characters")

        freq = WordFrequency(text)
        common_words = freq.get_frequency()
        freq.create_chart(common_words)

        db.execute("INSERT INTO texts (content) VALUES (?);", text)
        db.execute("UPDATE visits SET button_counts = button_counts + 1 WHERE ID = 786;")

        return render_template("analyzed.html")

    else:
        return render_template("index.html")

@app.route("/analyzed", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        db.execute("UPDATE visits SET download_count = download_count + 1 WHERE ID = 786;")
        return send_file("static/barchart.png", as_attachment=True)
    else:
        return render_template("analyzed.html")
