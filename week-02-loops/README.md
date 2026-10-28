# Week 02: Loops

## Number guessing game

[guessing_game.py](guessing_game.py) is a **starter exercise** for practicing `while` loops, `continue`, comparisons, functions, and input validation.

The computer chooses a random whole number from **1 to 20**. You have **five valid guesses** to find it. After each guess, the program tells you whether your number is too low or too high. Invalid entries do not use an attempt.

### Run the exercise

From the repository root:

```bash
python week-02-loops/guessing_game.py
```

The program uses only Python's standard library.

### Run the tests

```bash
python -m unittest discover -s week-02-loops -p "test_*.py" -v
```

The tests cover hints, invalid input, winning, running out of attempts, and cancelling when input ends.

### Try it yourself

1. Explain why `get_valid_guess()` uses a `while True` loop.
2. Change the maximum attempts from five to three.
3. Add a "very close" hint for guesses one or two numbers away.
4. After understanding the program, rewrite it independently without looking at the example.

This code is a provided learning example. The tasks above are **suggested practice**, not claimed completed work.
