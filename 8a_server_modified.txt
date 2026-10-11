
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    text_to_analyze = ""

    if request.method == "POST":
        text_to_analyze = request.form.get("textToAnalyze", "").strip()

        if not text_to_analyze:
            error = "Please enter some text to analyze."
        else:
            result = emotion_detector(text_to_analyze)

            if not result or result.get("dominant_emotion") is None:
                error = (
                    "Emotion detection is currently unavailable. "
                    "Please try again later."
                )

    return render_template(
        "index.html",
        result=result,
        error=error,
        text_to_analyze=text_to_analyze,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)