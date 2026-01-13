import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_multiple_children(self):
        first_child_node = LeafNode("b", "first_child")
        second_child_node = LeafNode("p", "second_child")
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>first_child</b><p>second_child</p></div>",
        )

    def test_to_html_with_multiple_children_and_parents(self):
        grandchild_node = LeafNode("p", "grandchild")
        first_child_node = ParentNode("b", [grandchild_node])
        second_child_node = LeafNode("p", "second_child")
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b><p>grandchild</p></b><p>second_child</p></div>",
        )



if __name__ == "__main__":
    unittest.main()