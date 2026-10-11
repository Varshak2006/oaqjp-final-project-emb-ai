
# Emotion Detection Application

## Project Description
A Python application that detects emotions in text using the IBM Watson NLP Emotion Detection service.

## Features
- Analyzes text for anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Provides a Flask web interface.
- Handles blank input and service errors.
- Includes unit tests.

## Technologies
- Python
- Requests
- Flask
- IBM Watson NLP Emotion Detection API
- unittest

## Run the Application
Install dependencies:

```bash
python -m pip install requests flask
```

Start the Flask application:

```bash
python server.py
```

Open http://127.0.0.1:5000 in your browser.

## Testing
Run the unit tests:

```bash
python -m unittest -v test_emotion_detection.py
```