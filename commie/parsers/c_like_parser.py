# SPDX-FileCopyrightText: Copyright (c) 2021 Art Galkin <ortemeo@gmail.com>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: BSD-3-Clause

# AG 2021: in pypi/comment_parser this module was only for parsing JavaScript.
# But in fact, it coped better with parsing C than regex-based c_parser.py.
# So for now it is the default parsed for all C-like languages.
#
# The most evident difference between JS and C in that single quotes can
# contain a string in JS, but in C and C++ they are only for single chars.
# However, for the task, individual characters within single quotes are
# hardly different from single-letter strings.

from enum import IntEnum, auto
from typing import Iterable, Optional

from commie.parsers import common
from commie.parsers.common import Comment, Span


def extract_comments(source: str) -> Iterable[Comment]:
	"""Extracts a list of comments from C-like source code.

	C-like comments come in two forms, single and multi-line comments.
	  - Single-line comments begin with '//' and continue to the end of line.
	  - Multi-line comments begin with '/*' and end with '*/' and can span
		multiple lines of code. If a multi-line comment does not terminate
		before EOF is reached, then an exception is raised.

	This module takes quoted strings into account when extracting comments from
	source code.
	"""

	class State(IntEnum):

		DEFAULT = auto()
		IN_SINGLE_LINE_COMMENT = auto()
		IN_MULTI_LINE_COMMENT = auto()
		IN_MULTI_LINE_COMMENT_AFTER_ASTERISK = auto()
		IN_STRING = auto()
		IN_STRING_AFTER_BACKSLASH = auto()
		FOUND_SLASH = auto()

	state: State = State.DEFAULT

	markup_start_pos = None
	text_start_pos: Optional[int] = 0
	# text_length: Optional[int] = 0

	quote = None
	position = 0

	for position, char in enumerate(source):

		if state == State.DEFAULT:
			# waiting for comment start character or beginning of a string
			if char == '/':
				state = State.FOUND_SLASH
			elif char in ('"', "'"):
				quote = char
				state = State.IN_STRING
		elif state == State.FOUND_SLASH:
			# found comment start character, classify next character and
			# determine if single or multi-line comment.
			if char == '/':
				state = State.IN_SINGLE_LINE_COMMENT
				markup_start_pos = position - 1  # we are at second char of "//"
				text_start_pos = position + 1
			elif char == '*':
				state = State.IN_MULTI_LINE_COMMENT
				markup_start_pos = position - 1  # we are at second char of "/*"
				text_start_pos = position + 1
			else:
				state = State.DEFAULT
		elif state == State.IN_SINGLE_LINE_COMMENT:
			# in single-line comment, reading characters until EOL
			if char == '\n':
				yield common.Comment(
					source,
					text_span=Span(text_start_pos, position),
					code_span=Span(markup_start_pos, position),
					multiline=False)
				text_length = 0
				state = State.DEFAULT
		# else:
		#	text_length += 1
		elif state == State.IN_MULTI_LINE_COMMENT:
			# in multi-line comment, add characters until '*' is
			# encountered.
			if char == '*':
				state = State.IN_MULTI_LINE_COMMENT_AFTER_ASTERISK
		# else:
		# text_length += 1
		elif state == State.IN_MULTI_LINE_COMMENT_AFTER_ASTERISK:
			# In multi-line comment with asterisk found. Determine if
			# comment is ending.
			if char == '/':
				yield Comment(
					source,
					text_span=Span(text_start_pos, position - 1),
					code_span=Span(markup_start_pos, position + 1),
					multiline=True)
				text_length = 0
				state = State.DEFAULT
			else:
				# text_length += 1
				# care for multiple '*' in a row
				if char != '*':
					# text_length += 1
					state = State.IN_MULTI_LINE_COMMENT
		elif state == State.IN_STRING:
			# in string literal, expect literal end or escape character.
			if char == quote:
				state = State.DEFAULT
			elif char == '\\':
				state = State.IN_STRING_AFTER_BACKSLASH
		elif state == State.IN_STRING_AFTER_BACKSLASH:
			state = State.IN_STRING
	# if char == '\n':
	# 	pass

	# end of file
	if state in (State.IN_MULTI_LINE_COMMENT, State.IN_MULTI_LINE_COMMENT_AFTER_ASTERISK):
		raise common.UnterminatedCommentError()

	if state == State.IN_SINGLE_LINE_COMMENT:
		yield common.Comment(
			source,
			text_span=Span(text_start_pos, position + 1),
			code_span=Span(markup_start_pos, position + 1),
			multiline=False)
