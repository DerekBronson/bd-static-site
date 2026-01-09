import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("No matching delimiter, not valid Markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            # No images to extract
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for i in range(len(matches)):
            sections = remaining_text.split(f"![{matches[i][0]}]({matches[i][1]})")
            if len(sections[0]) != 0:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(matches[i][0], TextType.IMAGE, matches[i][1]))
            if i == (len(matches) - 1):
                if len(sections[1]) != 0:
                    split_nodes.append(TextNode(sections[1], TextType.TEXT))
            remaining_text = sections[1]
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            # No links to extract
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for i in range(len(matches)):
            sections = remaining_text.split(f"[{matches[i][0]}]({matches[i][1]})")
            if len(sections[0]) != 0:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(matches[i][0], TextType.LINK, matches[i][1]))
            if i == (len(matches) - 1):
                if len(sections[1]) != 0:
                    split_nodes.append(TextNode(sections[1], TextType.TEXT))
            remaining_text = sections[1]
        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    delimiters = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]
    for delimiter in delimiters:
        nodes = split_nodes_delimiter(nodes, delimiter[0], delimiter[1])

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
