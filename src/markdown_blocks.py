from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        if block_to_block_type(block) == block_type_paragraph:
            html_node = paragraph_block_to_html_node(block)
        if block_to_block_type(block) == block_type_heading:
            html_node = heading_block_to_html_node(block)
        if block_to_block_type(block) == block_type_code:
            html_node = code_block_to_html_node(block)
        if block_to_block_type(block) == block_type_quote:
            html_node = quote_block_to_html_node(block)
        if block_to_block_type(block) == block_type_unordered_list:
            html_node = unordered_list_block_to_html_node(block)
        if block_to_block_type(block) == block_type_ordered_list:
            html_node = ordered_list_block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def block_to_block_type(block):
    lines = block.split("\n")
    if (block.startswith("# ") or block.startswith("## ") or block.startswith("### ") 
        or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_block_to_html_node(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_block_to_html_node(block):
    level = 0
    for char in block:
        if char != "#":
            break
        level += 1
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_block_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_block_to_html_node(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        stripped_lines.append(line.lstrip("> "))
    text = " ".join(stripped_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_block_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ordered_list_block_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)