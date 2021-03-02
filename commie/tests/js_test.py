# SPDX-FileCopyrightText: Copyright (c) 2021 Art Galkin <ortemeo@gmail.com>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: MIT

import unittest

from commie import js_parser, common


class JsParserTest(unittest.TestCase):

  def testSingleLineComment(self):
    code = '// single line comment'
    comments = list(js_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), "// single line comment")
    self.assertEqual(comments[0].text_span.extract(code), " single line comment")
    self.assertEqual(comments[0].multiline, False)

  def testLineCommentInSingleQuotedLiteral(self):
    code = "msg = '// this is not a comment'"
    comments = list(js_parser.extract_comments(code))
    self.assertEqual(len(comments), 0)

  def testLineCommentInDoubleQuotedLiteral(self):
    code = 'msg = "// this is not a comment"'
    comments = list(js_parser.extract_comments(code))
    self.assertEqual(len(comments), 0)

  def testMultiLineComment(self):
    code = '/* multiline\ncomment */'
    comments = list(js_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)
    self.assertEqual(comments[0].markup_span.extract(code), '/* multiline\ncomment */')
    self.assertEqual(comments[0].text_span.extract(code), " multiline\ncomment ")
    self.assertEqual(comments[0].multiline, True)


  def testMultiLineCommentWithStars(self):
    code = "/***************/"
    comments = list(js_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)
    self.assertEqual(comments[0].markup_span.extract(code), '/***************/')
    self.assertEqual(comments[0].text_span.extract(code), "*************")
    self.assertEqual(comments[0].multiline, True)

  def testMultiLineCommentInSingleLiteral(self):
    code = "msg = '/* This is not a\\nmultiline comment */'"
    comments = list(js_parser.extract_comments(code))
    self.assertEqual(len(comments), 0)

  def testMultiLineCommentInDoubleLiteral(self):
    code = 'msg = "/* This is not a\\nmultiline comment */"'
    comments = list(js_parser.extract_comments(code))
    self.assertEqual(len(comments), 0)

  def testMultiLineCommentUnterminated(self):
    code = 'a = 1 /* Unterminated\\n comment'
    with self.assertRaises(common.UnterminatedCommentError):
      list(js_parser.extract_comments(code))

  def testMultiple(self):
    code = """

    /*
     * this is a fancy comment
     * one more line of it
     */

    let forgetIt = prompt("What?");

    // bye!

    """

    comments = list(js_parser.extract_comments(code))

    self.assertEqual(len(comments), 2)
    self.assertEqual(comments[0].multiline, True)
    self.assertEqual(comments[1].multiline, False)
