# SPDX-FileCopyrightText: Copyright (c) 2021 Art Galkin <ortemeo@gmail.com>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: MIT

import unittest

from commie.parsers import common, go_parser


class GoParserTest(unittest.TestCase):

  def testSingleLineComment(self):
    code = '// single line comment'
    comments = list(go_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), "// single line comment")
    self.assertEqual(comments[0].text_span.extract(code), " single line comment")
    self.assertEqual(comments[0].multiline, False)

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

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), '/* multiline\ncomment */')
    self.assertEqual(comments[0].text_span.extract(code), " multiline\ncomment ")
    self.assertEqual(comments[0].multiline, True)

  def testMultiLineCommentWithStars(self):
    code = "/***************/"
    comments = list(go_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), "/***************/")
    self.assertEqual(comments[0].text_span.extract(code), "*************")
    self.assertEqual(comments[0].multiline, True)

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
