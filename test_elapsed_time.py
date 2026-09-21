"""Tests for elapsed-time formatting."""

import unittest

from elapsed_time import format_elapsed_time, format_time_ago


class FormatElapsedTimeTests(unittest.TestCase):
    def test_formats_seconds_and_fractional_seconds(self):
        self.assertEqual(format_elapsed_time(0), "0 seconds")
        self.assertEqual(format_elapsed_time(1), "1 second")
        self.assertEqual(format_elapsed_time(1.25), "1.25 seconds")

    def test_formats_larger_units(self):
        self.assertEqual(
            format_elapsed_time(90),
            "1 minute, 30 seconds",
        )
        self.assertEqual(
            format_elapsed_time(90_061.5),
            "1 day, 1 hour, 1 minute, 1.5 seconds",
        )

    def test_rejects_invalid_durations(self):
        with self.assertRaises(ValueError):
            format_elapsed_time(-1)
        with self.assertRaises(ValueError):
            format_elapsed_time(float("inf"))
        with self.assertRaises(TypeError):
            format_elapsed_time("1")


class FormatTimeAgoTests(unittest.TestCase):
    def test_uses_the_largest_whole_unit(self):
        self.assertEqual(format_time_ago(0), "0 seconds ago")
        self.assertEqual(format_time_ago(30.9), "30 seconds ago")
        self.assertEqual(format_time_ago(90), "1 minute ago")
        self.assertEqual(format_time_ago(7_200), "2 hours ago")
        self.assertEqual(format_time_ago(86_400), "1 day ago")
        self.assertEqual(format_time_ago(86_400 * 2), "2 days ago")
        self.assertEqual(format_time_ago(86_400 * 31), "31 days ago")

    def test_rejects_invalid_durations(self):
        with self.assertRaises(ValueError):
            format_time_ago(-1)
        with self.assertRaises(TypeError):
            format_time_ago("1")


if __name__ == "__main__":
    unittest.main()
