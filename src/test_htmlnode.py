import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("LeafNode(a, Click me!, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))


class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text")])
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_nesting_parents(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), 
                                ParentNode("p", [LeafNode("i", "italic text")])])
        self.assertEqual("<p><b>Bold text</b><p><i>italic text</i></p></p>", node.to_html())

    def test_repr(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text")])
        self.assertEqual("ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)", repr(node))


if __name__ == "__main__":
    unittest.main()