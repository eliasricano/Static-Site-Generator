from textnode import TextNode, TextType

def main():
    tn = TextNode("some text", TextType.ITALIC, "https://www.boot.dev")
    print(tn)

main()