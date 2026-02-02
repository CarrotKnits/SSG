

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
