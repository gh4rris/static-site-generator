import unittest

from inline_markdown import(
    split_nodes_delimiter,
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link)

from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image)

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
        
    def test_extract_no_image(self):
        text = "This is text with no image"
        self.assertEqual([], extract_markdown_images(text))
        
    
    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)", text_type_text)
        new_node = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with an ", text_type_text), 
                          TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
                          TextNode(" and ", text_type_text), 
                          TextNode("another", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")], new_node)
        
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", text_type_text)
        new_node =split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a ", text_type_text),
                          TextNode("link", text_type_link, "https://www.example.com"),
                          TextNode(" and ", text_type_text),
                          TextNode("another", text_type_link, "https://www.example.com/another")], new_node)

if __name__ == "__main__":
    unittest.main()