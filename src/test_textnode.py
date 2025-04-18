import unittest

from textnode import TextNode, TextType

class TestTextnode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_url(self):
        node = TextNode.url = None
     

if __name__ == "__main__":
    unittest.main()

    