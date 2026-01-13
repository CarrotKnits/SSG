import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
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

    def test_html_repr(self):
        node = HTMLNode("p", "Hello", ["children", "list"],{"class": "greeting"})
        rep = repr(node)
        self.assertIn("HTMLNode", rep)
        self.assertIn("p", rep)
        self.assertIn("Hello", rep)
        self.assertIn("children", rep)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("a", "Click", {"href": "https://x.com", "target": "_blank"})
        html = node.to_html()
        self.assertIn('<a ', html)
        self.assertIn('href="https://x.com"', html)
        self.assertIn('target="_blank"', html)
        self.assertIn('>Click</a>', html)

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello", {"class": "greeting"})
        rep = repr(node)
        self.assertIn("LeafNode", rep)
        self.assertIn("p", rep)
        self.assertIn("Hello", rep)

if __name__ == "__main__":
    unittest.main()