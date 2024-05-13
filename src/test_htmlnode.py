import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("h1", "heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("h1", "heading", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("HTMLNode(h1, heading, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))


if __name__ == "__main__":
    unittest.main()