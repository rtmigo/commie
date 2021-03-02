# SPDX-FileCopyrightText: Copyright (c) 2021 Art Galkin <ortemeo@gmail.com>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: MIT


import unittest

from commie import ruby_parser


class ShellParserTest(unittest.TestCase):

  def testComment(self):
    code = '# comment'
    comments = list(ruby_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.substring(code), '# comment')
    self.assertEqual(comments[0].text_span.substring(code), " comment")
    self.assertEqual(comments[0].multiline, False)

  def testCommentInSingleQuotedString(self):
    code = "'this is # not a comment'"
    comments = list(ruby_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testCommentInDoubleQuotedString(self):
    code = '"this is # not a comment"'
    comments = list(ruby_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testNestedStringSingleOutside(self):
    code = "'this is \"# not a comment\"'"
    comments = list(ruby_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testNestedStringDoubleOutside(self):
    code = '"this is \'# not a comment\'"'
    comments = list(ruby_parser.extract_comments(code))
    self.assertEqual(comments, [])

  def testEscapedSingleQuote(self):
    code = "\\'# this is a comment"
    comments = list(ruby_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.substring(code), '# this is a comment')
    self.assertEqual(comments[0].text_span.substring(code), " this is a comment")
    self.assertEqual(comments[0].multiline, False)

  def testEscapedDoubleQuote(self):
    code = '\\"# this is a comment'
    comments = list(ruby_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.substring(code), '# this is a comment')
    self.assertEqual(comments[0].text_span.substring(code), " this is a comment")
    self.assertEqual(comments[0].multiline, False)

  def testDoubleComment(self):
    code = '# this is not # another comment'
    comments = list(ruby_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.substring(code), '# this is not # another comment')
    self.assertEqual(comments[0].text_span.substring(code), ' this is not # another comment')
    self.assertEqual(comments[0].multiline, False)


  def testLiteralsSeparatedByComment(self):
    code = r"'This is' # 'a comment'"
    comments = list(ruby_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.substring(code), "# 'a comment'")
    self.assertEqual(comments[0].text_span.substring(code), " 'a comment'")
    self.assertEqual(comments[0].multiline, False)



  def testDifferentLiteralsSeparatedByComment(self):
    code = r''''This is' # "a comment"'''
    comments = list(ruby_parser.extract_comments(code))

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].markup_span.substring(code), '# "a comment"')
    self.assertEqual(comments[0].text_span.substring(code), ' "a comment"')
    self.assertEqual(comments[0].multiline, False)
