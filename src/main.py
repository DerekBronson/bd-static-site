from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(f"TextNode: {text_node}")

    html_node_details = {
        "tag": "a",
        "value": "https://www.boots.dev",
        "children": None,
        "props": {
            "href": "https://www.boots.dev",
            "target": "_blank",
        },
    }

    html_node = HTMLNode(**html_node_details)
    print(f"HTMLNode: {html_node}")
    print(f"HTML Node Props to HTML: {html_node.props_to_html()}")
    print(html_node.props.items())


if __name__ == "__main__":
    main()
