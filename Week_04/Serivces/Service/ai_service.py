from Serivces.Classifier.classifier import (
    Classifier,
)


class AIService:
    """Application service for AI-related operations."""

    def __init__(
        self,
        classifier: Classifier,
    ) -> None:

        self.classifier = classifier

    def classify(
        self,
        text: str,
    ) -> dict[str, str]:

        if not text.strip():
            raise ValueError(
                "Text cannot be empty."
            )

        category = self.classifier.classify(
            text
        )

        return {
            "text": text,
            "category": category,
        }