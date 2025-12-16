import unittest

import htmlnode
import main
import textnode


class TestConversion(unittest.TestCase):
    def test_text(self):
        node = textnode.TextNode("This is a text node", textnode.TextType.TEXT)
        html_node = main.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
