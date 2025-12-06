import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_HTML_aTag(self):
        node_details = {
            "tag": "a",
            "value": "https://www.boots.dev",
            "children": None,
            "props": {
                "href": "https://www.boots.dev",
                "target": "_blank",
            },
        }
        node = HTMLNode(**node_details)
        output = node.props_to_html()
        expected_output = 'href="https://www.boots.dev" target="_blank"'

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
