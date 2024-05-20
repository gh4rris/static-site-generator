import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownToHTML(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"], blocks)

    def test_markdown_to_blocks_newlines(self):
        markdown = "This is **bolded** paragraph\n\n\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"], blocks)