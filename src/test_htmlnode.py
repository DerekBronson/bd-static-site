import unittest

from htmlnode import HTMLNode, LeafNode


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
        node_details = {"tag": "p"}
        node = LeafNode(**node_details)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
