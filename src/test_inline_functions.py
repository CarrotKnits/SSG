import unittest
from textnode import TextNode, TextType
from inline_functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_multi_bold(self):
        node = TextNode("This is text with a **bolded** word and **another** one.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
                TextNode(" one.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_with_spaces(self):
        node = TextNode("This is text with a **bolded** word and **another one.**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another one.", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)

        # First handle bold
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        # Then handle italic on the result
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)

        nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            nodes,
        )

    def test_odd_delimiters_raises(self):
        node = TextNode("This is **broken bold", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_non_text_nodes_unchanged(self):
        node = TextNode("bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual([node], new_nodes)

    def test_no_delimiters_returns_same_node(self):
        node = TextNode("Just plain text, no markup here", TextType.TEXT)

        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertListEqual(
            [TextNode("Just plain text, no markup here", TextType.TEXT)],
            new_nodes,
        )


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )

    def test_extract_markdown_images_multiple(self):
        text = (
            "Look ![first](https://a.com/1.png) and "
            "also ![second](https://b.com/2.jpg)"
        )
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("first", "https://a.com/1.png"),
                ("second", "https://b.com/2.jpg"),
            ],
            matches,
        )

    def test_extract_markdown_images_none(self):
        text = "No images here, just text and [a link](https://boot.dev)"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_images_empty_alt(self):
        text = "An image with empty alt ![](https://example.com/img.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("", "https://example.com/img.png")],
            matches,
        )


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links_single(self):
        text = "Go [to boot dev](https://www.boot.dev) now"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")],
            matches,
        )

    def test_extract_markdown_links_multiple(self):
        text = (
            "Links: [first](https://a.com) and "
            "[second](https://b.com/path)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("first", "https://a.com"),
                ("second", "https://b.com/path"),
            ],
            matches,
        )

    def test_extract_markdown_links_ignores_images(self):
        text = (
            "An image ![alt](https://img.com/x.png) and a link "
            "[click](https://example.com)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("click", "https://example.com")],
            matches,
        )

    def test_extract_markdown_links_none(self):
        text = "No links or [broken(https://example.com"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)




if __name__ == "__main__":
    unittest.main()