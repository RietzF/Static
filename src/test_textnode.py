import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        node3 = TextNode("This is a chicken node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD, 'https://www.youtube.com')
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, 'https://www.youtube.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'https://www.youtube.com')
        self.assertEqual(node, node2)

        
  


if __name__ == "__main__":
    unittest.main()