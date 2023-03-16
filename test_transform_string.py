import unittest
from transform_string import tranform_string


class TestTransformString(unittest.TestCase):
    def setUp(self):
        self.complete_phrase = "this is an example string"
        self.empty_string = ""
        self.phrase_with_one_letter = "h"
        self.wrong_value_as_phrase_integer = 25
        self.wrong_value_as_phrase_complex_number = 25 + 5j
        self.wrong_value_as_phrase_boolean = False

        self.resul_example_string_transform = "tHIS iS aN eXAMPLE sTRING"
        self.result_one_letter_string_transfom = "h"

    def test_transform_string_grather_than_one_character(self):
        # test transform string when string length is grater than 0
        self.assertAlmostEqual(
            tranform_string(self.complete_phrase), self.resul_example_string_transform
        )
        self.assertAlmostEqual(
            tranform_string(self.phrase_with_one_letter),
            self.result_one_letter_string_transfom,
        )

    def test_transform_string_with_one_character(self):
        self.assertAlmostEqual(
            tranform_string(self.phrase_with_one_letter),
            self.result_one_letter_string_transfom,
        )

    def test_values(self):
        """Test value errors are raised when necesary"""
        self.assertRaises(ValueError, tranform_string, self.empty_string)

    def test_types(self):
        """Test type erroa are raised when necesary"""
        self.assertRaises(
            TypeError, tranform_string, self.wrong_value_as_phrase_integer
        )
        self.assertRaises(
            TypeError, tranform_string, self.wrong_value_as_phrase_complex_number
        )
        self.assertRaises(
            TypeError, tranform_string, self.wrong_value_as_phrase_boolean
        )
