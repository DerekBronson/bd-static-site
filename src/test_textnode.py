import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_noURL(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_URL(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_TextType_noURL(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq_TextType_URL(self):
        node = TextNode("This is a text node", TextType.TEXT, "http://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.IMAGE, "http://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_Text_noURL(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node with changes", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_not_eq_Text_URL(self):
        node = TextNode("This is a text node", TextType.LINK, "http://www.boot.dev")
        node2 = TextNode(
            "This is a text node with changes", TextType.IMAGE, "http://www.boot.dev"
        )
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
