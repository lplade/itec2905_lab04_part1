import unittest
from unittest.mock import patch
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




