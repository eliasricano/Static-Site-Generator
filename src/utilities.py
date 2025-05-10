from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        nodes = []
        if node.text_type != TextType.NORMAL:
            nodes.append(node)
            continue
            