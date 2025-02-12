import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    # Main Paths
    def test_props_eq(self):
        node = LeafNode("a", "Poop clicker!", {"href": "https://www.google.com"})
        string = '<a href="https://www.google.com">Poop clicker!</a>'
        print("LEAF_NODE_TEST:",node.to_html(), '\n-----',string)
        self.assertEqual(node.to_html(), string)

    def test_no_value(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode(None, None, None)
            node.to_html()
        self.assertEqual(str(context.exception), "INVALID: All leaf nodes MUST have a value")

    def test_no_tag(self):
        node = LeafNode(None, "This text has no tag!")
        string = 'This text has no tag!'
        print("NO TAG:",node.to_html(), '\n-----',string)
        self.assertEqual(node.to_html(), string)

    # Edge Cases

        