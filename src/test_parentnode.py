import unittest

from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    # Main Paths
    def test_no_tag(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, "This text has no tag!", None)
            node.to_html()
        print("PARENT NO TAG:",str(node.to_html()), '\n-----', "INVALID: All parent nodes MUST have a tag")
        self.assertEqual(str(context.exception), "INVALID: All parent nodes MUST have a tag")

    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("a", None, None)
            node.to_html()
        print("PARENT NO CHILDREN:",str(node.to_html()), '\n-----', "INVALID: All parent nodes MUST have children. Otherwise they aren't parents. It's only logic bro.")
        self.assertEqual(str(context.exception), "INVALID: All parent nodes MUST have children. Otherwise they aren't parents. It's only logic bro.")
