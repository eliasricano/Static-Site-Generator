import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node, node2, "Nodes are equal")

    def test_notEq(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2, "Nodes are different")

    def test_NoneUrl(self):
        node = TextNode("This is a code node", TextType.CODE)
        self.assertIsNone(node.url, "property is None")

if __name__ == "__main__":
    unittest.main()