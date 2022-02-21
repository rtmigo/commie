# SPDX-FileCopyrightText: Copyright (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: BSD-3-Clause

import unittest
from typing import List

from .. import iter_comments_python, Comment


def commentsToList(code: str) -> List[Comment]:
	return list(iter_comments_python(code))


class PythonParserTest(unittest.TestCase):

	def testEmptyString(self):
		code = ""
		comments = commentsToList(code)
		self.assertEqual(len(comments), 0)

	def testComment(self):
		code = '# comment'
		comments = commentsToList(code)

		self.assertEqual(len(comments), 1)

		self.assertEqual(comments[0].code, '# comment')
		self.assertEqual(comments[0].text, " comment")
		self.assertEqual(comments[0].multiline, False)

	def testCommentInSingleQuotedString(self):
		code = "'this is # not a comment'"
		comments = commentsToList(code)
		self.assertEqual(comments, [])

	def testCommentInDoubleQuotedString(self):
		code = '"this is # not a comment"'
		comments = commentsToList(code)
		self.assertEqual(comments, [])

	def testNestedStringSingleOutside(self):
		code = "'this is \"# not a comment\"'"
		comments = commentsToList(code)
		self.assertEqual(comments, [])

	def testNestedStringDoubleOutside(self):
		code = '"this is \'# not a comment\'"'
		comments = commentsToList(code)
		self.assertEqual(comments, [])

	def testEscapedSingleQuote(self):
		code = "\\'# this is a comment"
		comments = commentsToList(code)

		self.assertEqual(len(comments), 1)

		self.assertEqual(comments[0].code, "# this is a comment")
		self.assertEqual(comments[0].text, " this is a comment")
		self.assertEqual(comments[0].multiline, False)

	def testEscapedDoubleQuote(self):
		code = '\\"# this is another comment'
		comments = commentsToList(code)

		self.assertEqual(len(comments), 1)

		self.assertEqual(comments[0].code, "# this is another comment")
		self.assertEqual(comments[0].text, " this is another comment")
		self.assertEqual(comments[0].multiline, False)
