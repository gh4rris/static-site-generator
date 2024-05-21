import unittest

from markdown_blocks import(
    markdown_to_blocks, 
    block_to_block_type,
    markdown_to_html_node,
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

    def test_paragraphs_to_html(self):
        text = "The first paragraph has **bold** text\n\nand the second has *italic* text"
        node = markdown_to_html_node(text)
        html = node.to_html()
        self.assertEqual("<div><p>The first paragraph has <b>bold</b> text</p><p>and the second has <i>italic</i> text</p></div>", html)

    def test_headings_to_html(self):
        text = "# This is a heading\n\nThis paragraph has some `code` in it\n\n## This is a second heading"
        node = markdown_to_html_node(text)
        html = node.to_html()
        self.assertEqual("<div><h1>This is a heading</h1><p>This paragraph has some <code>code</code> in it</p><h2>This is a second heading</h2></div>", html)

    def test_quote_to_html(self):
        text = "> This is\n> a blockquote\n\nand this is a paragraph"
        node = markdown_to_html_node(text)
        html = node.to_html()
        self.assertEqual("<div><blockquote>This is a blockquote</blockquote><p>and this is a paragraph</p></div>", html)

    def test_unordered_list_to_html(self):
        text = "* first item\n* second item\n* third item"
        node = markdown_to_html_node(text)
        html = node.to_html()
        self.assertEqual("<div><ul><li>first item</li><li>second item</li><li>third item</li></ul></div>", html)

    def test_ordered_list_to_html(self):
        text = "1. first item\n2. second item\n3. third item\n\nparagraph"
        node = markdown_to_html_node(text)
        html = node.to_html()
        self.assertEqual("<div><ol><li>first item</li><li>second item</li><li>third item</li></ol><p>paragraph</p></div>", html)


if __name__ == "__main__":
    unittest.main()