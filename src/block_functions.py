from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType, TextNode, text_node_to_html_node
from inline_functions import text_to_textnodes

def markdown_to_blocks(markdown): # markdown is a raw Markdown string: represents a full document
    final_blocks = []
    striped_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        striped_blocks.append(block.strip(" \n"))
    for block in striped_blocks:
        if block != "":
            final_blocks.append(block)
    return final_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif block.lstrip().startswith(">"):
        return BlockType.QUOTE
    elif block.lstrip().startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if line.strip() == "":
                continue
            if not line.lstrip().startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.lstrip().startswith("1. "):
        counter = 1
        lines = block.split("\n")
        for line in lines:
            if line.strip() == "":
                continue
            if not line.lstrip().startswith(f"{counter}. "):
                return BlockType.PARAGRAPH
            counter += 1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

# helper functions for 'markdown_to_html_node()' -------------------------------------------------------------

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def block_to_paragraph(block):
    text = block.replace("\n", " ")
    text = " ".join(text.split())
    node = ParentNode("p", text_to_children(text), props=None)
    return node

def block_to_heading(block):
    hashtag_count = len(block) - len(block.lstrip("#"))
    stripped = block[hashtag_count:]
    text = stripped.lstrip(" ")
    if hashtag_count == 1:
        node = ParentNode("h1", text_to_children(text), props=None)
        return node
    elif hashtag_count == 2:
        node = ParentNode("h2", text_to_children(text), props=None)
        return node
    elif hashtag_count == 3:
        node = ParentNode("h3", text_to_children(text), props=None)
        return node
    elif hashtag_count == 4:
        node = ParentNode("h4", text_to_children(text), props=None)
        return node
    elif hashtag_count == 5:
        node = ParentNode("h5", text_to_children(text), props=None)
        return node
    elif hashtag_count == 6:
        node = ParentNode("h6", text_to_children(text), props=None)
        return node

def block_to_quote(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        line = line.lstrip()
        if line.strip() == "":
            continue     
        stripped = line.removeprefix("> ").removeprefix(">")
        stripped_lines.append(stripped)
    text = "\n".join(stripped_lines)
    children = text_to_children(text)
    node = ParentNode("blockquote", children, props=None)
    return node

def block_to_unordered_list(block):
    li_children = []
    lines = block.split("\n")
    for line in lines:
        line = line.lstrip()
        if line.strip() == "":
            continue
        stripped = line.removeprefix("* ").removeprefix("- ")
        inline_children = text_to_children(stripped)
        li_node = ParentNode("li", inline_children, props=None)
        li_children.append(li_node)
    node = ParentNode("ul", li_children, props=None)
    return node

def block_to_ordered_list(block):
    li_children = []
    lines = block.split("\n")
    for line in lines:
        line.lstrip()
        if line.strip() == "":
            continue
        _, stripped = line.split(". ", 1)
        inline_children = text_to_children(stripped)
        li_node = ParentNode("li", inline_children, props=None)
        li_children.append(li_node)
    node = ParentNode("ol", li_children, props=None)
    return node

def block_to_code(block):
    lines = block.split("\n")
    inner_lines = lines[1:-1]
    cleaned_lines = [line.lstrip() for line in inner_lines if line.strip() != ""]
    joined = "\n".join(cleaned_lines) + "\n"
    text_node = TextNode(joined, TextType.TEXT, None)
    leaf = text_node_to_html_node(text_node)
    code_node = ParentNode("code", [leaf])
    pre_node = ParentNode("pre", [code_node])
    return pre_node

#----------------------------------------------------------------------

def markdown_to_html_node(markdown): # parameter is a full Markdown docment
    div_children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            node = block_to_paragraph(block)
            div_children.append(node)

        elif block_type == BlockType.HEADING:
            node = block_to_heading(block)
            div_children.append(node)

        elif block_type == BlockType.QUOTE:
            node = block_to_quote(block)
            div_children.append(node)

        elif block_type == BlockType.UNORDERED_LIST:
            node = block_to_unordered_list(block)
            div_children.append(node)

        elif block_type == BlockType.ORDERED_LIST:
            node = block_to_ordered_list(block)
            div_children.append(node)

        elif block_type == BlockType.CODE:
            node = block_to_code(block)
            div_children.append(node)

    div = ParentNode("div", div_children, props=None)
    return div



