import re
from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image)

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        if extract_markdown_images(node.text) == []:
            new_nodes.append(node)
            continue
        image_tuples = extract_markdown_images(node.text)
        original_text = node.text
        for tuple in image_tuples:
            split_text = original_text.split(f"![{tuple[0]}]({tuple[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(tuple[0], text_type_image, tuple[1]))
            original_text = split_text[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
            
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        if extract_markdown_links(node.text) == []:
            new_nodes.append(node)
            continue
        link_tuples = extract_markdown_links(node.text)
        original_text = node.text
        for tuple in link_tuples:
            split_text = original_text.split(f"[{tuple[0]}]({tuple[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(tuple[0], text_type_link, tuple[1]))
            original_text = split_text[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, text_type_text)
    bold = split_nodes_delimiter([node], "**", text_type_bold)
    italic = split_nodes_delimiter(bold, "*", text_type_italic)
    code = split_nodes_delimiter(italic, "`", text_type_code)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link