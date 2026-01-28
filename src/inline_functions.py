from textnode import TextType, TextNode
import re


# Returns a new list of nodes, where any "text" type nodes in the input
# list are (potentially) split into multiple nodes based on the syntax.

# e.g. // node = TextNode("This is text with a `code block` word", TextType.TEXT)
#         new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#   Expected OUTPUT:
#         [
#             TextNode("This is text with a ", TextType.TEXT),
#             TextNode("code block", TextType.CODE),
#             TextNode(" word", TextType.TEXT),
#         ]

def split_nodes_delimiter(old_nodes, delimiter, text_type): # old_nodes = list, delimiter = str, text_type = text type
    new_nodes_list = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes_list.append(old_node)
            continue
        else:
            text_parts = old_node.text.split(delimiter)
            delimiter_count = len(text_parts) - 1
            if delimiter_count % 2 != 0:
                raise Exception("Invalid Markdown syntax")
            for i, part in enumerate(text_parts):
                if part == "":
                    continue # skip empty strings
                if i % 2 == 0:
                    # outside delimiters -> plain text
                    node_type = TextType.TEXT
                else:
                    # inside delimiters -> special text
                    node_type = text_type
                new_nodes_list.append(TextNode(part, node_type))
    return new_nodes_list
                    

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes_list = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes_list.append(old_node)
            continue
        if old_node.text == "":
            continue
        images = extract_markdown_images(old_node.text)
        if images == []:
            new_nodes_list.append(old_node)      
        else:
            current_text = old_node.text
            for alt, url in images:
                text_parts = current_text.split(f"![{alt}]({url})", 1)
                if text_parts[0] == "":
                    pass
                else:
                    new_nodes_list.append(TextNode(text_parts[0], TextType.TEXT))
                new_nodes_list.append(TextNode(alt, TextType.IMAGE, url))
                current_text = text_parts[1]
            if current_text == "":
                pass
            else:
                new_nodes_list.append(TextNode(current_text, TextType.TEXT))
    return new_nodes_list

def split_nodes_link(old_nodes):
    new_nodes_list = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes_list.append(old_node)
            continue
        if old_node.text == "":
            continue
        links = extract_markdown_links(old_node.text)
        if links == []:
            new_nodes_list.append(old_node)      
        else:
            current_text = old_node.text
            for alt, url in links:
                text_parts = current_text.split(f"[{alt}]({url})", 1)
                if text_parts[0] == "":
                    pass
                else:
                    new_nodes_list.append(TextNode(text_parts[0], TextType.TEXT))
                new_nodes_list.append(TextNode(alt, TextType.LINK, url))
                current_text = text_parts[1]
            if current_text == "":
                pass
            else:
                new_nodes_list.append(TextNode(current_text, TextType.TEXT))
    return new_nodes_list