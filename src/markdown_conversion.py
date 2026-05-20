from blocks import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    # Runs sub fuctions (one per block type) that return a bunch of leafnodes
    # Get the block type first
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordList_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordList_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    # Returns a Parent node and any relevant children based on parsing the paragraph
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def heading_to_html_node(block):
    header_count = 0
    for char in block:
        if char == "#":
            header_count += 1
        else:
            break
    if header_count == 0:
        raise ValueError("No headers in header block")
    if header_count >= len(block):
        raise ValueError("Header count is higher than length of the block")
    text = block[header_count + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{header_count}", children)


def ordList_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        parts = line.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def unordList_to_html_node(block):
    lines = block.split("\n")
    clean_lines = [line.lstrip("- ") for line in lines]
    list_items = []
    for line in clean_lines:
        children = text_to_children(line)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    clean_lines = [line.lstrip("> ") for line in lines]
    paragraph = " ".join(clean_lines)
    children = text_to_children(paragraph)
    return ParentNode("blockquote", children)  # Fill in
