import os
import sys
import unittest
from unittest.mock import mock_open, patch

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from main import extract_title


class ExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        # Test case 1: Title found at the beginning of the file
        mock_md_content_1 = "# My Title\nSome other content."
        with patch("builtins.open", mock_open(read_data=mock_md_content_1)):
            self.assertEqual(extract_title("dummy_path.md"), "My Title")

    def test_leading_spaces(self):
        # Test case 2: Title found with leading spaces (should not be a title)
        mock_md_content_2 = " # Not a Title\n# Actual Title"
        with patch("builtins.open", mock_open(read_data=mock_md_content_2)):
            self.assertEqual(extract_title("dummy_path.md"), "Actual Title")

    def test_no_title(self):
        # Test case 3: No title found
        mock_md_content_3 = "No title here.\nAnother line."
        with patch("builtins.open", mock_open(read_data=mock_md_content_3)):
            self.assertEqual(extract_title("dummy_path.md"), "")

    def test_empty_file(self):
        # Test case 4: Empty file
        mock_md_content_4 = ""
        with patch("builtins.open", mock_open(read_data=mock_md_content_4)):
            self.assertEqual(extract_title("dummy_path.md"), "")

    def test_multiple_hash(self):
        # Test case 5: Multiple hash marks (should only consider single hash for title)
        mock_md_content_5 = "## Not a Title\n# This is the Title"
        with patch("builtins.open", mock_open(read_data=mock_md_content_5)):
            self.assertEqual(extract_title("dummy_path.md"), "This is the Title")

    def test_special_characters(self):
        # Test case 6: Title with special characters
        mock_md_content_6 = "# Title with !@#$%^&*()_+\nContent."
        with patch("builtins.open", mock_open(read_data=mock_md_content_6)):
            self.assertEqual(extract_title("dummy_path.md"), "Title with !@#$%^&*()_+")

    def test_title_with_numbers(self):
        # Test case 7: Title with numbers
        mock_md_content_7 = "# Title 123\nContent."
        with patch("builtins.open", mock_open(read_data=mock_md_content_7)):
            self.assertEqual(extract_title("dummy_path.md"), "Title 123")


if __name__ == "__main__":
    unittest.main()
