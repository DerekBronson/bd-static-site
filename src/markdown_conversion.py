from blocks import block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    # Runs sub fuctions (one per block type) that return a bunch of leafnodes
