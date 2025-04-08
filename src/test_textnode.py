import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    # Test for when both TextNodes are Equal
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.IMAGES)
        self.assertNotEqual(node, node2)

    # Test for when Url is None
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    # Test that all text_type's are equal
    def test_text_type_different(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.NORMAL)
        node4 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.CODE)
        node6 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node5, node6)

        node7 = TextNode("This is a text node", TextType.LINKS)
        node8 = TextNode("This is a text node", TextType.LINKS)
        self.assertEqual(node7, node8)

        node9 = TextNode("This is a text node", TextType.IMAGES)
        node10 = TextNode("This is a text node", TextType.IMAGES)
        self.assertEqual(node9, node10)

        node11 = TextNode("This is a text node", TextType.BOLD)
        node12 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node11, node12)

    # Test for when both TextNodes are Not Equal
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

# Test function 'text_node_to_html_node'
class TestTextNodeToHTMLNodeFunction(unittest.TestCase):
    # Main paths

    def test_text_node_to_html_node_text(self):
        # Test conversion of plain text nodes - should have no tag, just value
        text_node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertIsNone(html_node.tag, "Plain text node should not have a tag")
        self.assertEqual(html_node.value, "This is a text node", "Text value should be preserved exactly")
        self.assertEqual(html_node.props, {}, "Plain text node should not have any properties")

    def test_text_node_to_html_node_bold(self):
        # Test conversion of bold text - should have 'b' tag
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b", "Bold text should have 'b' tag")
        self.assertEqual(html_node.value, "Bold text", "Bold text value should be preserved")
        self.assertEqual(html_node.props, {}, "Bold node should not have any properties")

    def test_text_node_to_html_node_italic(self):
        # Test conversion of italic text - should have 'i' tag
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i", "Italic text should have 'i' tag")
        self.assertEqual(html_node.value, "Italic text", "Italic text value should be preserved")
        self.assertEqual(html_node.props, {}, "Italic node should not have any properties")

    def test_text_node_to_html_node_code(self):
        # Test conversion of code text - should have 'code' tag
        text_node = TextNode("print('hello')", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code", "Code text should have 'code' tag")
        self.assertEqual(html_node.value, "print('hello')", "Code text value should be preserved")
        self.assertEqual(html_node.props, {}, "Code node should not have any properties")

    def test_text_node_to_html_node_link(self):
        # Test conversion of link - should have 'a' tag and href property
        text_node = TextNode("Click me", TextType.LINKS, "https://boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a", "Link should have 'a' tag")
        self.assertEqual(html_node.value, "Click me", "Link text should be preserved")
        self.assertEqual(html_node.props["href"], "https://boot.dev", "Link should have correct href property")

    def test_text_node_to_html_node_image(self):
        # Test conversion of image - should have 'img' tag with src and alt properties
        text_node = TextNode("My Image", TextType.IMAGES, "https://boot.dev/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img", "Image should have 'img' tag")
        self.assertEqual(html_node.value, "", "Image node should have empty string value")
        self.assertEqual(html_node.props["src"], "https://boot.dev/image.png", "Image should have correct src property")
        self.assertEqual(html_node.props["alt"], "My Image", "Image should have alt text from node text")

if __name__ == "__main__":
    unittest.main()

