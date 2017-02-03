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

    @patch("builtins.input", side_effect=["one", "20", "3", "7", "5"])
    @patch("builtins.print")
    def test_play_a_game(self, mock_print, mock_input):
        high = 9
        low = 0

        # Save ref
        random_function = guess.generate_random_number

        # Replace random function with constant
        guess.generate_random_number = Mock(return_value=5)

        # Run the program
        guess.main(low, high)

        mock_input.assert_called_with("What number am I thinking of? ")

        # Get the args sent to mock print()
        printcalls = mock_print.call_args_list

        # We should get the following outputs in order
        expected_out_strings = [
            "That's not an integer!",
            "That is not between " + str(low) + " and " + str(high) + "!",
            "Sorry, your number is too low.",
            "Sorry, your number is too high.",
            "You got it! I picked " + str(5) + "."
        ]
        # Loop over these
        # i+1 because there's an intro print()
        for i in range(5):
            # note the second parameter has to be a tuple
            self.assertEqual(printcalls[i+1][0], (expected_out_strings[i],))

        # Restore ref
        guess.generate_random_number = random_function







