from enum import Enum


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
    elif block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if line.startswith(">"):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if line.startswith("- "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith("1."):
        counter = 1
        lines = block.split("\n")
        for line in lines:
            if line.startswith(f"{counter}. "):
                counter += 1
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    

def markdown_to_blocks(markdown): # markdown is a raw Markdown string: represents a full document
    final_blocks = []
    striped_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        striped_blocks.append(block.strip())
    for block in striped_blocks:
        if block != "":
            final_blocks.append(block)
    return final_blocks
