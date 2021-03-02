#!/usr/bin/python
"""Tests for comment_parser.parsers.go_parser.py"""

import unittest
from comment_parser.parsers import common, go_parser


@unittest.skip # todo
class GoParserTest(unittest.TestCase):

  def testSingleLineComment(self):
    code = '// single line comment'
    comments = list(go_parser.extract_comments(code))
    print(comments)
    exit()
    expected = [common.Comment(code[2:], 1, multiline=False)]
    self.assertEqual(comments, expected)

  def testSingleLineCommentInRuneLiteral(self):
    code = "msg := '// this is not a comment'"
    comments = list(go_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testSingleLineCommentInBackTickedLiteral(self):
    code = "msg := `// this is not a comment`"
    comments = list(go_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testSingleLineCommentInQuotedLiteral(self):
    code = 'msg := "// this is not a comment"'
    comments = list(go_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testMultiLineComment(self):
    code = '/* multiline\ncomment */'
    comments = list(go_parser.extract_comments(code))
    print(comments)
    exit()
    expected = [common.Comment(code[2:-2], 1, multiline=True)]
    self.assertEqual(comments, expected)

  def testMultiLineCommentWithStars(self):
    code = "/***************/"
    comments = list(go_parser.extract_comments(code))
    print(comments)
    exit()
    expected = [common.Comment(code[2:-2], 1, multiline=True)]
    self.assertEqual(comments, expected)

  def testMultiLineCommentInRuneLiteral(self):
    code = "msg := '/* This is not a\\nmultiline comment */'"
    comments = list(go_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testMultiLineCommentInQuotedLiteral(self):
    code = 'msg := "/* This is not a\\nmultiline comment */"'
    comments = list(go_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testMultiLineCommentInBackTickedLiteral(self):
    code = 'msg := `/* This is not a\\nmultiline comment */`'
    comments = list(go_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testMultiLineCommentUnterminated(self):
    code = 'a := 1 /* Unterminated\\n comment'
    with self.assertRaises(common.UnterminatedCommentError):
      list(go_parser.extract_comments(code))
