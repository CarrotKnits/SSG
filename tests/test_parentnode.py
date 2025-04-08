import unittest

from htmlnode import ParentNode, LeafNode
from textnode import TextNode, text_node_to_html_node

class TestParentNode(unittest.TestCase):
    # Main Paths
    def test_no_tag(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, "This text has no tag!", None)
            node.to_html()
        self.assertEqual(str(context.exception), "INVALID: All parent nodes MUST have a tag")

    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("a", None, None)
            node.to_html()
        self.assertEqual(str(context.exception), "INVALID: All parent nodes MUST have children. Otherwise they aren't parents. It's only logic bro.")

    def test_one_child(self):
        node = ParentNode("p", [LeafNode("b", "Bold text")], None)
        string = '<p><b>Bold text</b></p>'
        self.assertEqual(node.to_html(), string)

    def test_multiple_children(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode("i", "Italic text"),
            LeafNode("u", "Underlined text")
        ], None)
        string = '<p><b>Bold text</b><i>Italic text</i><u>Underlined text</u></p>'
        self.assertEqual(node.to_html(), string)

    def test_parent_with_props(self):
        children = [LeafNode("b", "Fancy text")]
        props = {"class": "fancy", "id": "main"}
        node = ParentNode("div", children, props)
        string = '<div class="fancy" id="main"><b>Fancy text</b></div>'
        self.assertEqual(node.to_html(), string)

    def test_mixed_children(self):
        node = ParentNode("div", [
            LeafNode(None, "Plain text"),
            ParentNode("p", [LeafNode("b", "Bold text")], None),
            LeafNode(None, "More text")
        ], None)
        string = '<div>Plain text<p><b>Bold text</b></p>More text</div>'
        self.assertEqual(node.to_html(), string)

    def test_deeply_nested(self):
        node = ParentNode("div", [
            ParentNode("div", [
                ParentNode("p", [
                    ParentNode("span", [
                        LeafNode("b", "Deep text")
                    ], None)
                ], None)
            ], None)
        ], None)
        string = '<div><div><p><span><b>Deep text</b></span></p></div></div>'
        self.assertEqual(node.to_html(), string)
    
    def test_mixed_tag_types(self):
        node = ParentNode("p", [
            LeafNode(None, "Plain text"),
            LeafNode("b", "Bold text"),
            LeafNode(None, "More plain text")
        ], None)
        string = '<p>Plain text<b>Bold text</b>More plain text</p>'
        self.assertEqual(node.to_html(), string)