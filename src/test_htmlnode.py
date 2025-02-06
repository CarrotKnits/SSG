import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    # Main Paths
    def test_props_eq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
        string = 'href="https://www.google.com" target="_blank"'
        print("PtoHTML:",node.props_to_html(), '\nSTRING:',string)
        self.assertEqual(node.props_to_html(), string)

    def test_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_props_one_prop(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com"})
        string = 'href="https://www.google.com"'
        print("PtoHTML:",node.props_to_html(), '\nSTRING:',string)
        self.assertEqual(node.props_to_html(), string)


    # Edge Cases
    def test_props_empty_dict(self):
        node = HTMLNode(None, None, None, {})
        self.assertEqual(node.props_to_html(), '')

    def test_props_space_in_key(self):
        node = HTMLNode(None, None, None, {"id id": "weird", "target": "_blank",})
        string = 'id id="weird" target="_blank"'
        print("PtoHTML:",node.props_to_html(), '\nSTRING:',string)
        self.assertEqual(node.props_to_html(), string)

    # Failure Cases