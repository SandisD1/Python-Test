import contextlib
import io
import unittest

from task_modules import second_task


class TestSecondTask(unittest.TestCase):

    def test_with_correct_numbers(self):
        expected_output = "assertions are correct"
        x = 5
        y = 10

        captured_output = io.StringIO()

        with contextlib.redirect_stdout(captured_output):
            second_task.math_assertions(x, y)

        captured_string = captured_output.getvalue().strip()

        self.assertEqual(expected_output, captured_string, "Test failed")

    def test_with_incorrect_numbers(self):
        x = 10
        y = 5
        with self.assertRaises(AssertionError):
            second_task.math_assertions(x, y)
