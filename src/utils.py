import re
from textnode import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    nodes_list = []
    for node in old_nodes:
        new_nodes = []
        if node.text_type != TextType.NORMAL:
            nodes_list.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown at text node: %s" % node.text)
        for i in range(len(parts)):
            if i == 0 or i % 2 == 0:
                new_text_node = TextNode(parts[i], TextType.NORMAL)
                new_nodes.append(new_text_node)
            else:
                new_text_node = TextNode(parts[i], text_type)
                new_nodes.append(new_text_node)
        nodes_list.extend(new_nodes)
    return nodes_list

def extract_markdown_images(text: str) -> list[tuple[str, str]]: 
    match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            template = f"![{image[0]}]({image[1]})"
            sections = original_text.split(template, 1)
            if len(sections) != 2:
                raise Exception("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1]
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            template = f"[{link[0]}]({link[1]})"
            sections = original_text.split(template, 1)
            if len(sections) != 2:
                raise Exception("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1]
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes

