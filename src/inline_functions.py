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
                    # outside selimiters -> plain text
                    node_type = TextType.TEXT
                else:
                    # inside delimiters -> special text
                    node_type = text_type

                new_nodes_list.append(TextNode(part, node_type))
                    

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

