import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    testing_props = {"href": "https://www.google.com", "target": "_blank",}

    def test_props_string(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
        return node