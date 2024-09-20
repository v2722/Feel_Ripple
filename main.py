from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os

nltk.download('vader_lexicon')

# Set template_folder to the current directory
app = Flask(__name__, template_folder='.')

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        if score["neg"] != 0:
            return render_template('index.html', message="negative comment!😥😔")
        else:
            return render_template('index.html', message="positive comment!😇🙂")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
