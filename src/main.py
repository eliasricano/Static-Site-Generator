from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    my_list = [1, 2]
    other_list = [3, 4]
    my_list.append(other_list)
    print(my_list)

main()