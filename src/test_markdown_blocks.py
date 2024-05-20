import unittest

from markdown_blocks import(
    markdown_to_blocks, 
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list)

class TestMarkdownToHTML(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"], blocks)

    def test_markdown_to_blocks_newlines(self):
        markdown = "This is **bolded** paragraph\n\n\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"], blocks)

    
    def test_block_to_block_type(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote1\n> quote2"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* unordered1\n* unordered2"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "- unordered1\n- unordered2"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. ordered1\n2. ordered2"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)


if __name__ == "__main__":
    unittest.main()