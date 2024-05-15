import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code)

class TestInLineMarkdown(unittest.TestCase):

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual([TextNode("This is text with a ", text_type_text),
                          TextNode("code block", text_type_code),
                          TextNode(" word", text_type_text)], new_nodes)
        
    def test_non_text_type_text(self):
        node = TextNode("This node is an italic text type", text_type_italic)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual([TextNode("This node is an italic text type", text_type_italic, None)], new_nodes)

    def test_multiple_bold(self):
        node = TextNode("This is **bold** and so **is this**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual([TextNode("This is ", text_type_text),
                          TextNode("bold", text_type_bold),
                          TextNode(" and so ", text_type_text),
                          TextNode("is this", text_type_bold)], new_nodes)
        
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual([("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
                          ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")], extract_markdown_images(text))
        
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual([("link", "https://www.example.com"), 
                          ("another", "https://www.example.com/another")], extract_markdown_links(text))
        

if __name__ == "__main__":
    unittest.main()