# SPDX-FileCopyrightText: Copyright (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: BSD-3-Clause

"""This module provides methods for parsing comments from HTML family languages.

Works with:
  HTML
  XML
  SGML
"""

import re
from typing import Iterable

import commie.x01_errors
from commie.parsers._helper import matchGroupToComment
from commie.x01_common import Comment


def extract_comments(htmlCode: str) -> Iterable[Comment]:
	"""Extracts a list of comments from the given HTML family source code.

	Comments are represented with the Comment class found in the common module.
	HTML family comments come in one form, comprising all text within '<!--' and
	'-->' markers. Comments cannot be nested.

	Args:
	  htmlCode: String containing code to extract comments from.
	Returns:
	  Python list of common.Comment in the order that they appear in the code..
	Raises:
	  common.UnterminatedCommentError: Encountered an unterminated multi-line
		comment.
	"""
	pattern = r"""
		(?P<literal> (\"([^\"\n])*\")+) |
		(?P<single> <!--(?P<single_content>.*?)-->) |
		(?P<multi> <!--(?P<multi_content>(.|\n)*?)?-->) |
		(?P<error> <!--(.*)?)
	  """
	compiled = re.compile(pattern, re.VERBOSE | re.MULTILINE)

	for match in compiled.finditer(htmlCode):

		kind = match.lastgroup

		if kind == "single":
			# all the comments in HTML are multi-line
			yield matchGroupToComment(match, "single_content", True)
		elif kind == "multi":
			yield matchGroupToComment(match, "multi_content", True)
		elif kind == "error":
			raise commie.x01_errors.UnterminatedCommentError()
