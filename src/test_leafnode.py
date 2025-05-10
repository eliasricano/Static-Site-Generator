import unittest
from leafnode import *
from textnode import *

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link to google", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com">Link to google</a>')
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_to_html(self):
        node = TextNode("This is a bold text", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": None})
    
    def test_text_to_html_img(self):
        node = TextNode("This is an image", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {"src": None, "alt": None})