import unittest
from unittest.mock import patch
import guess


class TestGuessingGame(unittest.TestCase):

    @patch("builtins.input",
           side_effect=[
               "0", "1", "147", "-54", "tacos", ""
           ])
    @patch("builtins.print")
    def test_input_guess(self, mock_print, mock_input):

        return_values = [
            0, 1, 147, -54, None, None
        ]

        for test in return_values:
            guess.input_guess()
            mock_print.assert_called_with(test)




