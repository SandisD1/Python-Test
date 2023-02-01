import contextlib
import io
import unittest

from task_modules import third_task


class TestThirdTask(unittest.TestCase):

    def test_with_default_input(self):
        search_str = "ABC"
        expected = f"{search_str} found with key - type"
        search_dict = {
            "book": "151012",
            "identifier": [
                {"type": "ABC", "value": "3806768526"},
                {"type": "DEF", "value": "97789689"},
            ],
        }

        captured_output = io.StringIO()

        with contextlib.redirect_stdout(captured_output):
            third_task.find_value(search_dict, search_str)

        captured_string = captured_output.getvalue().strip()

        self.assertEqual(expected, captured_string, "Test failed")

    def test_with_custom_input(self):
        search_str = "DEF"
        expected = f"{search_str} found with key - identifier"
        search_dict = {
            "book": {"name": "Big book", "pages": "400"},
            "identifier": "DEF"
        }

        captured_output = io.StringIO()

        with contextlib.redirect_stdout(captured_output):
            third_task.find_value(search_dict, search_str)

        captured_string = captured_output.getvalue().strip()

        self.assertEqual(expected, captured_string, "Test failed")

    def test_when_nothing_found(self):
        search_str = "BCD"
        expected = f"No {search_str} found"
        search_dict = {
            "book": "151012",
            "identifier": [
                {"type": "ABC", "value": "3806768526"},
                {"type": "DEF", "value": "97789689"},
            ],
        }

        captured_output = io.StringIO()

        with contextlib.redirect_stdout(captured_output):
            third_task.find_value(search_dict, search_str)

        captured_string = captured_output.getvalue().strip()

        self.assertEqual(expected, captured_string, "Test failed")
