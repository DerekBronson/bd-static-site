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
    def test_to_html_with_children_and_props(self):
        child_node = LeafNode(
            tag="a", value="Click me!", props={"href": "https://example.com"}
        )
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><a href="https://example.com">Click me!</a></div>',
        )

    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode(tag="b", value="grandchild", props={"class": "bold"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b class="bold">grandchild</b></span></div>',
        )

    def test_to_html_with_several_children_and_props(self):
        child_node = [
            LeafNode(tag="b", value="Bold text", props={"class": "bold"}),
            LeafNode(tag=None, value="Normal text"),
            LeafNode(tag="i", value="Italic text", props={"class": "italic"}),
            LeafNode(tag=None, value="Normal text"),
        ]
        parent_node = ParentNode("p", child_node)
        self.assertEqual(
            parent_node.to_html(),
            '<p><b class="bold">Bold text</b>Normal text<i class="italic">Italic text</i>Normal text</p>',
        )

    def test_to_html_with_props_on_parent(self):
        child_node = LeafNode(tag="b", value="Bold text")
        parent_node = ParentNode("div", [child_node], {"class": "parent"})
        self.assertEqual(
            parent_node.to_html(), '<div class="parent"><b>Bold text</b></div>'
        )

    def test_to_html_with_empty_children_list(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_deeper_nesting(self):
        great_grandchild_node = LeafNode("b", "great-grandchild")
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        expected_html = "<div><p><span><b>great-grandchild</b></span></p></div>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_mixed_children(self):
        children = [
            LeafNode("b", "Bold text"),
            ParentNode("div", [LeafNode("i", "Italic in a div")]),
            LeafNode(None, "Normal text"),
        ]
        parent_node = ParentNode("p", children)
        expected_html = (
            "<p><b>Bold text</b><div><i>Italic in a div</i></div>Normal text</p>"
        )
        self.assertEqual(parent_node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
