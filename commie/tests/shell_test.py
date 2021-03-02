# SPDX-FileCopyrightText: Copyright (c) 2021 Art Galkin <ortemeo@gmail.com>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: MIT

import unittest

from commie import shell_parser


class ShellParserTest(unittest.TestCase):

  def testComment(self):
    code = '# comment'
    comments = list(shell_parser.extract_comments(code))
    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), '# comment')
    self.assertEqual(comments[0].text_span.extract(code), " comment")
    self.assertEqual(comments[0].multiline, False)

  def testEscapedComment(self):
    code = r'\# not a comment'
    comments = list(shell_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testCommentInSingleQuotedString(self):
    code = "'this is # not a comment'"
    comments = list(shell_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testCommentInDoubleQuotedString(self):
    code = '"this is # not a comment"'
    comments = list(shell_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testNestedStringSingleOutside(self):
    code = "'this is \"# not a comment\"'"
    comments = list(shell_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testNestedStringDoubleOutside(self):
    code = '"this is \'# not a comment\'"'
    comments = list(shell_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testEscapedSingleQuote(self):
    code = "\\'# this is a comment"
    comments = list(shell_parser.extract_comments(code))
    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), "# this is a comment")
    self.assertEqual(comments[0].text_span.extract(code), " this is a comment")
    self.assertEqual(comments[0].multiline, False)

  def testEscapedDoubleQuote(self):
    code = '\\"# this is another comment'
    comments = list(shell_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.extract(code), "# this is another comment")
    self.assertEqual(comments[0].text_span.extract(code), " this is another comment")
    self.assertEqual(comments[0].multiline, False)

