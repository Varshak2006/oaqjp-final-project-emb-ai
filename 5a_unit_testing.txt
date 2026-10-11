
import unittest
from unittest.mock import patch, Mock

from emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    @patch("emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.02,
                        "joy": 0.95,
                        "sadness": 0.01,
                    }
                }]
            },
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.95,
                        "disgust": 0.01,
                        "fear": 0.01,
                        "joy": 0.02,
                        "sadness": 0.01,
                    }
                }]
            },
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.95,
                        "fear": 0.01,
                        "joy": 0.01,
                        "sadness": 0.02,
                    }
                }]
            },
        )
        result = emotion_detector("I feel disgusted")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.02,
                        "joy": 0.01,
                        "sadness": 0.95,
                    }
                }]
            },
        )
        result = emotion_detector("I am so sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("emotion_detection.requests.post")
    def test_fear(self, mock_post):
        mock_post.return_value = Mock(
            status_code=200,
            json=lambda: {
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.95,
                        "joy": 0.01,
                        "sadness": 0.02,
                    }
                }]
            },
        )
        result = emotion_detector("I am really afraid")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()