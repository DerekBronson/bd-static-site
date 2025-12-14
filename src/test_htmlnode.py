import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_HTML_href(self):
        node_details = {
            "props": {
                "href": "https://www.boots.dev",
                "target": "_blank",
            },
        }
        node = HTMLNode(**node_details)
        output = node.props_to_html()
        expected_output = 'href="https://www.boots.dev" target="_blank"'

        self.assertEqual(output, expected_output)

    def test_props_to_HTML_None(self):
        node_details = {
            "tag": "a",
        }
        node = HTMLNode(**node_details)
        output = node.props_to_html()
        expected_output = ""

        self.assertEqual(output, expected_output)

    def test_props_to_HTML_Empty(self):
        node_details = {
            "tag": "a",
            "props": "",
        }
        node = HTMLNode(**node_details)
        output = node.props_to_html()
        expected_output = ""

        self.assertEqual(output, expected_output)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node_details = {
            "tag": "p",
            "value": "Hello, world!",
        }
        node = LeafNode(**node_details)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node_details = {
            "tag": "a",
            "value": "Click me!",
            "props": {
                "href": "https://www.google.com",
            },
        }
        node = LeafNode(**node_details)
        expected_output = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_output)

    def test_leaf_to_html_no_value(self):
        node_details = {
            "tag": "p",
            "value": None,
        }
        node = LeafNode(**node_details)
        with self.assertRaises(ValueError):
            node.to_html()


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_several_children(self):
        child_node = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ]
        parent_node = ParentNode("p", child_node)
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_no_tag(self):
        parent_node = ParentNode(None, "Text")
        with self.assertRaises(ValueError):
            parent_node.to_html()

    # ---START HERE AND UPDATE THESE TO USE PROPS---
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_several_children(self):
        child_node = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ]
        parent_node = ParentNode("p", child_node)
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
        )


if __name__ == "__main__":
    unittest.main()
