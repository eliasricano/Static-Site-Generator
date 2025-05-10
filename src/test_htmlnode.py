import unittest

from htmlnode import *
from textnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Text inside p", None, None)
        node2 = HTMLNode("p", "Text inside p", None, None)
        self.assertEqual(node, node2)

    def test_notEq(self):
        node = HTMLNode("p", "Text inside p", None, None)
        node2 = HTMLNode("a", "Text inside a", None, {"href", "www.google.com"})
        self.assertNotEqual(node, node2)

    def test_noneChildren(self):
        node = HTMLNode("p", "Text inside p", None, None)
        self.assertIsNone(node.children)

    