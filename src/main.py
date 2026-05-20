from markdown_conversion import markdown_to_html_node


def main():
    md = """
# Heading 1

## Heading 2

###### Heading 6
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    print(f"HTML for the node is {html}")


if __name__ == "__main__":
    main()
