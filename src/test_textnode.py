import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url_not_eq(self):
        node1 = TextNode("sample text", TextType.ITALIC, url ="https://example.com")
        node2 = TextNode("sample text", TextType.ITALIC, url ="https://different.com")
        self.assertNotEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()