# SPDX-FileCopyrightText: Copyright (c) 2021 Art Galkin <ortemeo@gmail.com>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: MIT

import unittest

from commie.parsers import common, html_parser


class ShellParserTest(unittest.TestCase):

  def testComment(self):
    code = '<!--comment-->'
    comments = list(html_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), "<!--comment-->")
    self.assertEqual(comments[0].text_span.extract(code), "comment")
    self.assertEqual(comments[0].multiline, False)

  def testMultilineComment(self):
    code = '<!--multi-line\ncomment-->'
    comments = list(html_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), '<!--multi-line\ncomment-->')
    self.assertEqual(comments[0].text_span.extract(code), "multi-line\ncomment")
    self.assertEqual(comments[0].multiline, True)

  def testTwoSeparateSingleComment(self):
    code = '<!--comment1-->\n<!--comment2-->'
    comments = list(html_parser.extract_comments(code))

    self.assertEqual(len(comments), 2)

    self.assertEqual(comments[0].markup_span.extract(code), '<!--comment1-->')
    self.assertEqual(comments[0].text_span.extract(code), "comment1")
    self.assertEqual(comments[0].multiline, False)

    self.assertEqual(comments[1].markup_span.extract(code), '<!--comment2-->')
    self.assertEqual(comments[1].text_span.extract(code), "comment2")
    self.assertEqual(comments[1].multiline, False)

  def testLayeredComment(self):
    code = '<!-- comment<!-- -->'
    comments = list(html_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), '<!-- comment<!-- -->')
    self.assertEqual(comments[0].text_span.extract(code), " comment<!-- ")
    self.assertEqual(comments[0].multiline, False)

  def testNonGreedyComment(self):
    code = '<!--i am a comment--> not a comment -->'
    comments = list(html_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), '<!--i am a comment-->')
    self.assertEqual(comments[0].text_span.extract(code), "i am a comment")
    self.assertEqual(comments[0].multiline, False)

  def testSideBySideComment(self):
    code = '<!--comment1--> ... <!--comment2-->'
    comments = list(html_parser.extract_comments(code))

    self.assertEqual(len(comments), 2)

    self.assertEqual(comments[0].markup_span.extract(code), '<!--comment1-->')
    self.assertEqual(comments[0].text_span.extract(code), "comment1")
    self.assertEqual(comments[0].multiline, False)

    self.assertEqual(comments[1].markup_span.extract(code), '<!--comment2-->')
    self.assertEqual(comments[1].text_span.extract(code), "comment2")
    self.assertEqual(comments[1].multiline, False)

  def testUnterminatedComment(self):
    code = '<!--invalid'
    with self.assertRaises(common.UnterminatedCommentError):
      list(html_parser.extract_comments(code))

  def testLonelyTerminator(self):
    code = 'not a comment-->'
    comments = list(html_parser.extract_comments(code))
    self.assertEqual(comments, [])
