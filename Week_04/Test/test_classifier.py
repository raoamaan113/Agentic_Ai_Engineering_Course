from Serivces.Classifier.rule_classifier import RuleClassifier
from Serivces.Classifier.keyword_classifier import KeywordClassifier


# --- original 4 test cases ---


def test_password_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I forgot my password")

    assert result == "account"


def test_fee_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I have a fee problem")

    assert result == "finance"


def test_technical_classification():
    classifier = RuleClassifier()

    result = classifier.classify("The server is down")

    assert result == "technical"


def test_unknown_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I want some information")

    assert result == "other"


# --- 6 NEW TEST CASES (TOTAL: 10) ---


def test_case_insensitivity_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("RESET MY PASSWORD IMMEDIATELY")

    assert result == "account"


def test_payment_finance_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("My billing statement shows an extra payment charge")

    assert result == "finance"


def test_database_technical_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("The connection failed with a timeout error on the API")

    assert result == "technical"


def test_empty_string_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("")

    assert result == "other"


def test_whitespace_and_punctuation_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("  Help!   Login Issue?   ")

    assert result == "account"


def test_general_query_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("Hello, what are your opening hours?")

    assert result == "other"