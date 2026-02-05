import unittest

from block_functions import markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node


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


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
    >This is a
    > multi-line _quote_
    >that is **uninspiring**
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a\nmulti-line <i>quote</i>\nthat is <b>uninspiring</b></blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
    - is in no
    - This list
    - particular
    - unordered
    - order, hence
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>is in no</li><li>This list</li><li>particular</li><li>unordered</li><li>order, hence</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
    1. This list
    2. is in a
    3. particular
    4. order
    5. hence, ordered
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This list</li><li>is in a</li><li>particular</li><li>order</li><li>hence, ordered</li></ol></div>",
        )

    #def test_heading(self):


    #def test_multiple_headings(self):