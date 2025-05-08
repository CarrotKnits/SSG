import unittest
from inline import split_nodes_delimiter, extract_markdown_images
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        # CODE delimiter "`"
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        # Assert the result has 3 nodes
        self.assertEqual(len(result), 3)
        
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.NORMAL)


    def test_bold_delimiter(self):
        # BOLD delimiter "**"
        node = TextNode("This is text with a **booooold** word", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        # Assert the result has 3 nodes
        self.assertEqual(len(result), 3)
        
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        
        self.assertEqual(result[1].text, "booooold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.NORMAL)


    def test_italic_delimiter(self):
        # ITALIC delimiter "_"
        node = TextNode("This is text with an _ItalicItalic_ word", TextType.NORMAL)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        # Assert the result has 3 nodes
        self.assertEqual(len(result), 3)
        
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with an ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        
        self.assertEqual(result[1].text, "ItalicItalic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.NORMAL)


    def test_no_delimiter(self):
        # No delimiter / NORMAL text
        plain_node = TextNode("Just plain text", TextType.NORMAL)
        plain_result = split_nodes_delimiter([plain_node], "`", TextType.CODE)
        
        # Result should be the same node
        self.assertEqual(len(plain_result), 1)
        self.assertEqual(plain_result[0].text, "Just plain text")
        self.assertEqual(plain_result[0].text_type, TextType.NORMAL)


    def test_unclosed_delimiter(self):
        # Test for unclosed delimiter
        node = TextNode("This is text with an _ItalicItalic word", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "_", TextType.ITALIC)


    def test_multiple_nodes_same_delimiter(self):
        # Multiple text nodes in the input
        nodes = [
            TextNode("This is text with an _ItalicItalic_ word", TextType.NORMAL),
            TextNode("This is OTHER text with an _ItalicItalic_ word", TextType.NORMAL),
            TextNode("This is YET MORE text with an _ItalicItalic_ word", TextType.NORMAL)
        ]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        # Assert the result has the correct number of resulting nodes
        self.assertEqual(len(result), 9)  # Each input node splits into 3

        # Check the content and type of the first node
        self.assertEqual(result[0].text, "This is text with an ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        self.assertEqual(result[1].text, "ItalicItalic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.NORMAL)

        # Check content and type for a node in the middle
        self.assertEqual(result[3].text, "This is OTHER text with an ")
        self.assertEqual(result[3].text_type, TextType.NORMAL)
        self.assertEqual(result[4].text, "ItalicItalic")
        self.assertEqual(result[4].text_type, TextType.ITALIC)
        self.assertEqual(result[5].text, " word")
        self.assertEqual(result[5].text_type, TextType.NORMAL)

        # Check content and type for the third node
        self.assertEqual(result[6].text, "This is YET MORE text with an ")
        self.assertEqual(result[6].text_type, TextType.NORMAL)
        self.assertEqual(result[7].text, "ItalicItalic")
        self.assertEqual(result[7].text_type, TextType.ITALIC)
        self.assertEqual(result[8].text, " word")
        self.assertEqual(result[8].text_type, TextType.NORMAL)


class TestExtractMarkdownImages(unittest.TestCase):
    # test extraction of images
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    # test if ignores links
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an [link](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([], matches)