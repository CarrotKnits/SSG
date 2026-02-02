import unittest

from block_functions import markdown_to_blocks, BlockType, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):
    def test_multiple_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_one_block(self):
        md = """
- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- This is a list\n- with items",
            ],
        )

    def test_no_blocks(self):
        md = """



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,[],)

    def test_repeated_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line






- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# heading"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_invalid_heading(self):
        block = "#invalid heading becomes a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_heading_6(self):
        block = "###### heading"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_code(self):
        block = """```
This is a code block
that is not filled with
poop or pee.
        ```"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_quote_with_space(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_quote_with_no_space(self):
        block = ">This is quote with no space after the symbol"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_multiple_quotes(self):
        block = """>This is a quote with no space after the symbol
> poop quote
> last quote"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_unordered_list(self):
        block = """- This is a list
- in order
- that is not"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_ordered_list(self):
        block = """1. This is a list
2. that is
3. in order"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_multiline_paragraph(self):
        block = """This is a multiline
paragraph.
Yes it is."""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_single_line_paragraph(self):
        block = "This is a single line paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)


