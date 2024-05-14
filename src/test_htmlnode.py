import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("h1", "heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("h1", "heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("HTMLNode(h1, heading, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual('<p>This is a paragraph of text.</p>', node.to_html())

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual('<a href="https://www.google.com" target="_blank">Click me!</a>', node.to_html())

    def test_value_error(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = LeafNode(None, "This node has no tag.")
        self.assertEqual("This node has no tag.", node.to_html())


if __name__ == "__main__":
    unittest.main()