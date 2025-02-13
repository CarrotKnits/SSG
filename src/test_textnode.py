import unittest

from textnode import TextNode, TextType


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



if __name__ == "__main__":
    unittest.main()

