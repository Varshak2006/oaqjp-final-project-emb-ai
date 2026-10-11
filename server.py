"""Flask server for the emotion detection final project."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the supplied text and return the emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Please enter some text to analyze."

    result = emotion_detector(text_to_analyze)

    if not result:
        return "Emotion detection is unavailable. Please try again later."

    if "emotionPredictions" in result:
        emotions = result["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
    else:
        emotions = result
        dominant_emotion = result.get("dominant_emotion")

    if dominant_emotion is None:
        return "Invalid text or emotion detection unavailable."

    return (
        "For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

