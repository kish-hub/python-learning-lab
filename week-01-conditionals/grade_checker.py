"""Practice comparisons and if/elif/else decisions."""


def describe_score(score: float) -> str:
    """Return a practice label for a score between 0 and 100."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 80:
        return "Excellent"
    if score >= 60:
        return "Good"
    if score >= 40:
        return "Keep practicing"
    return "Needs improvement"


if __name__ == "__main__":
    try:
        score = float(input("Enter a score from 0 to 100: "))
        print(describe_score(score))
    except ValueError as exc:
        print(f"Invalid input: {exc}")
