"""This module processes emotion predictions."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("emotionDetector")

"""This function executes emotion predictions."""
@app.route("/emotionDetector")
def sent_analyzer():
    """This function executes emotion predictions."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, 'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
)


@app.route("/")
def render_index_page():
    """This function executes emotion predictions."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
