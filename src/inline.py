from textnode import TextType
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type): #old_nodes is a list
    new_nodes = []

    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = old_node.text

        # Find first occurrence of opening delimiter
        start_index = text.find(delimiter)

        # If no delimiter found, keep node as is
        if start_index == -1:
            new_nodes.append(old_node)
            continue

        # Find closing delimiter (starting search after opening one)
        end_index = text.find(delimiter, start_index = len(delimiter))

        # If no closing delimiter found, raise exception
        if end_index == -1:
            raise ValueError(f"No closin delimiter '{delimiter}' found in text: {text}")
        
        # Extract the three parts of text
        before_start_delimiter = text[:start_index]
        between_delimiters = text[start_index + len(delimiter):end_index]
        after_closing_delimiter = text[end_index + len(delimiter):]

        #Create nodes for each part (only if not empty)
        if before_start_delimiter:
            new_nodes.append(TextNode(before_start_delimiter, TextType.NORMAL))

        #####
        # Create node from the delimited content with corrosponding text type
        new_nodes.append(TextNode(between_delimiters, text_type))

        # If there is text after closing delimiter
        if after_closing_delimiter:
            remaining_node = TextNode(after_closing_delimiter, TextType.NORMAL)

            # Recursively process this remaining text to find more delimiters
            additional_nodes = split_nodes_delimiter([remaining_node], delimiter, text_type)

            new_nodes.extend(additional_nodes)
    
    return new_nodes