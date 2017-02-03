import unittest
from unittest.mock import Mock, patch
import guess


class TestGuessingGame(unittest.TestCase):

    def test_input_guess(self):

        input_expected_output = {
            "0"    : 0,
            "1"    : 1,
            "145"  : 145,
            "-45"  : -45,
            "4.2"  : None,
            "tacos": None,
            ""     : None
        }

        for input_val in input_expected_output.keys():
            with patch("builtins.input", return_value=input_val) as mock_input:
                self.assertEqual(guess.input_guess(),
                                 input_expected_output[input_val])

    def test_respond_high_low(self):

        target = 5
        guess_expected_output = {
            0: False,
            3: False,
            5: True,
            7: False,
            9: False
        }

        for value in guess_expected_output.keys():
            self.assertEqual(guess.respond_low_high(target, value),
                             guess_expected_output[value])

    def test_test_if_in_range(self):
        low = 0
        high = 9
        guess_expected_output = {
            -1: False,
            0 : True,
            9 : True,
            10: False,
            400: False
        }

        for value in guess_expected_output.keys():
            self.assertEqual(guess.test_if_in_range(value, low, high),
                             guess_expected_output[value])

    @patch("guess.generate_random_number", return_value=5)
    @patch("guess.input_guess", side_effect=["one", "20", "3", "7", "5"])
    @patch("builtins.print")
    def test_play_a_game(self, mock_print, mock_input, mock_random):
        high = 9
        low = 0
        guess.main(low, high)

        mock_input.assert_called_with("What number am I thinking of? ")

        mock_print.assert_any_call("That's not an integer!")
        mock_print.assert_any_call("That number is not between"
                                   + str(low) + " and "
                                   + str(high) + "!")
        mock_print.assert_any_call("Sorry, your number is too low.")
        mock_print.assert_any_call("Sorry, your number is too high.")
        mock_print.assert_any_call("You got it! I picked " +
                                   str(5))







