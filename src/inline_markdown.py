import re
from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes =[]
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            for i in range(len(split_text)):
                if i % 2 == 0 and split_text[i] != "":
                    new_nodes.append(TextNode(split_text[i], text_type_text))
                elif split_text[i] != "":
                    new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
print(extract_markdown_links(text))