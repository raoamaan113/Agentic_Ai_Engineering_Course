from Serivces.Service.ai_service import AIService


class FakeClassifier:

    def classify(
        self,
        text: str,
    ) -> str:

        return "test-category"


def test_ai_service_uses_classifier():

    classifier = FakeClassifier()

    service = AIService(
        classifier
    )

    result = service.classify(
        "Any text"
    )

    assert result == {
        "text": "Any text",
        "category": "test-category",
    }