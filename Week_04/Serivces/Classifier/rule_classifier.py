class RuleClassifier:
    """Simple classifier implementation."""

    def classify(
        self,
        text: str,
    ) -> str:

        text = text.strip().lower()

        if not text:
            return "other"

        if "password" in text or "login" in text:
            return "account"

        if any(
            keyword in text
            for keyword in ("fee", "billing", "payment", "charge")
        ):
            return "finance"

        if (
            "server" in text
            or "api" in text
        ):
            return "technical"

        if "admission" in text:
            return "admission"

        return "other"

if __name__ == "__main__":

    classifier = RuleClassifier()

    print(
        classifier.classify(
            "I forgot my password"
        )
    )

    print(
        classifier.classify(
            "My fee payment is missing"
        )
    )

    print(
        classifier.classify(
            "The API server is down"
        )
    )