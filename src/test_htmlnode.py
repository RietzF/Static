import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_href(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')


if __name__ == "__main__":
    unittest.main()