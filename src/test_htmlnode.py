import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')
    
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        # Note: The order of attributes might vary, so you might need to adjust this test
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')
    
    def test_props_to_html_with_no_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")