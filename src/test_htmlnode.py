import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    testing_props = {"href": "https://www.google.com", "target": "_blank",}

    def test_props_eq(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
        string =  'href="https://www.google.com" target="_blank"'
        print("PtoHTML:",node.props_to_html(), '\nSTRING:',string)
        self.assertEqual(node.props_to_html(), string)