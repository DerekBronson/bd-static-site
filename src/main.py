from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def main():
    return


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return HTMLNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return HTMLNode(
            tag="a",
            value=text_node.url,
            children=None,
            props={"href": text_node.url, "target": "_blank"},
        )
    elif text_node.text_type == TextType.IMAGE:
        return HTMLNode(
            tag="img",
            value=text_node.url,
            children=None,
            props={"src": text_node.url, "alt": text_node.alt_text},
        )
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")


if __name__ == "__main__":
    main()
