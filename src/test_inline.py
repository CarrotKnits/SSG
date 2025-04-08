import unittest
from inline import split_nodes_delimiter
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
        node = TextNode("This is text with a _ItalicItalic_ word", TextType.NORMAL)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        # Assert the result has 3 nodes
        self.assertEqual(len(result), 3)
        
        # Check the content and type of each node
        self.assertEqual(result[0].text, "This is text with a ")
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

        # Test for unclosed delimiter


        # Test for invalid delimiter


        # Multiple text nodes in the input


        # Non-NORMAL nodes in the input


        # Invalid nodes in the input


        #Consecutive delimiters