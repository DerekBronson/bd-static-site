import unittest

from blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
)


class TestExtractText(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multi_empty(self):
        md = """
        This is a **bolded** paragraph




        This is the _final_ line with italics
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is the _final_ line with italics",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_md_to_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_md_to_quote(self):
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)

    def test_md_to_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item"), BlockType.UNORDERED_LIST)

    def test_md_to_ordered_list(self):
        self.assertEqual(block_to_block_type("1. Item"), BlockType.ORDERED_LIST)

    def test_md_to_code(self):
        self.assertEqual(
            block_to_block_type("```python\nprint('Hello, World!')\n```"),
            BlockType.CODE,
        )

    def test_md_to_paragraph(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH
        )

    def test_md_to_paragraph_with_newline(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph\n\nThis is another paragraph"),
            BlockType.PARAGRAPH,
        )

    def test_md_to_paragraph_with_newline_and_space(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph\n\n This is another paragraph"),
            BlockType.PARAGRAPH,
        )

    def test_md_to_paragraph_with_newline_and_space_and_tab(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph\n\n\tThis is another paragraph"),
            BlockType.PARAGRAPH,
        )

    def test_md_to_paragraph_with_newline_and_space_and_tab_and_space(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph\n\n\t This is another paragraph"),
            BlockType.PARAGRAPH,
        )
