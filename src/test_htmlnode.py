import unittest

from htmlnode import HTMLNode


class TextHTMLNode(unittest.TestCase):
    def test_eq_default(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq_args(self):
        node = HTMLNode(
            tag="tag",
            value="value",
            children=["children", "list"],
            props={"props":"dictionary"}
            )
        node2 = HTMLNode(
            tag="tag",
            value="value",
            children=["children", "list"],
            props={"props":"dictionary"}
            )
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(
            tag="tag",
            value="value",
            children=["poopy", "list"],
            props={"props":"dictionary"}
            )
        node2 = HTMLNode(
            tag="tag",
            value="value",
            children=["children", "list"],
            props={"props":"dictionary"}
            )
        self.assertNotEqual(node, node2)

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_default(self):
        node = HTMLNode(
            tag="p",
            props={"href": "https://example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://example.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode(
            tag="p",
            props=None
            )
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()