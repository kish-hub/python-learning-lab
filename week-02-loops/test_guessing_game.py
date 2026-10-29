"""Standard-library tests for the Week 02 guessing-game example."""

import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).with_name("guessing_game.py")
spec = importlib.util.spec_from_file_location("guessing_game", SCRIPT)
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


class GuessingGameTests(unittest.TestCase):
    def test_guess_hints(self):
        self.assertEqual(game.check_guess(4, 10), "Too low.")
        self.assertEqual(game.check_guess(16, 10), "Too high.")
        self.assertEqual(game.check_guess(10, 10), "Correct!")

    def test_invalid_input_is_retried(self):
        answers = ["hello", "0", "21", "12"]
        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=io.StringIO) as output:
                self.assertEqual(game.get_valid_guess(), 12)
        self.assertIn("Please enter a whole number.", output.getvalue())
        self.assertIn("Choose a number from 1 to 20.", output.getvalue())

    def test_correct_guess_ends_game(self):
        with patch.object(game.random, "randint", return_value=10):
            with patch("builtins.input", return_value="10"):
                with patch("sys.stdout", new_callable=io.StringIO) as output:
                    game.play_game()
        self.assertIn("Correct!", output.getvalue())
        self.assertIn("You found it in 1 attempt(s).", output.getvalue())

    def test_attempt_limit_reveals_answer(self):
        with patch.object(game.random, "randint", return_value=10):
            with patch("builtins.input", side_effect=["1"] * game.MAX_ATTEMPTS):
                with patch("sys.stdout", new_callable=io.StringIO) as output:
                    game.play_game()
        self.assertEqual(output.getvalue().count("Too low."), 5)
        self.assertIn("Out of attempts. The number was 10.", output.getvalue())

    def test_end_of_input_cancels_game(self):
        with patch.object(game.random, "randint", return_value=10):
            with patch("builtins.input", side_effect=EOFError):
                with patch("sys.stdout", new_callable=io.StringIO) as output:
                    game.play_game()
        self.assertIn("Game cancelled.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
