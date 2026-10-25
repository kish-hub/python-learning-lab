# Practicing Python functions, user input, and string formatting.
"""A simple introduction to functions, strings, and user input."""


def greet(name: str) -> str:
    """Create a greeting, using a default when the name is blank."""
    cleaned_name = name.strip()
    if not cleaned_name:
        cleaned_name = "friend"
    return f"Hello, {cleaned_name}! Welcome to Python."


if __name__ == "__main__":
    name = input("What is your name? ")
    print(greet(name))
