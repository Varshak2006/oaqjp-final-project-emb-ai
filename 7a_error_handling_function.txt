
import requests


def emotion_detector(text_to_analyze):
    """Analyze text using the Watson NLP emotion detection service."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            url, headers=headers, json=payload, timeout=30
        )

        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }

        response.raise_for_status()
        result = response.json()

        # Extract the emotion predictions from the Watson response.
        predictions = result["emotionPredictions"][0]["emotion"]

        scores = {
            "anger": predictions["anger"],
            "disgust": predictions["disgust"],
            "fear": predictions["fear"],
            "joy": predictions["joy"],
            "sadness": predictions["sadness"],
        }
        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores

    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }