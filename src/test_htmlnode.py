import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("h1", "Hello, world!")
        node3 = LeafNode("h2", "Hello, world!")
        node4 = LeafNode("h3", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "<h1>Hello, world!</h1>")
        self.assertEqual(node3.to_html(), "<h2>Hello, world!</h2>")
        self.assertEqual(node4.to_html(), "<h3>Hello, world!</h3>")

class TestParentnode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )