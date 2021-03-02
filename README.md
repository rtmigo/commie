# [rtmigo / commie.python](https://github.com/rtmigo/commie.python/)
[![Actions Status](https://github.com/rtmigo/commie.python/workflows/CI/badge.svg?branch=master)](https://github.com/rtmigo/commie.python/actions)
[![PyPI status](https://img.shields.io/pypi/status/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI license](https://img.shields.io/pypi/l/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/commie.svg)](https://pypi.python.org/pypi/commie/)

# Usage 

```python
from pathlib import Path
import commie

sourceCode=Path("/path/to/mycode.go").read_text()

for comment in commie.iter_comments_go(sourceCode):
 
  # comment code: "/* sample */"
  print("Comment inner text:", comment.text_span.extract(sourceCode))
  print("Comment text location:", comment.text_span.start, comment.text_span.end)
  
  # comment text: " sample "
  print("Comment code:", comment.markup_span.extract(sourceCode))
  print("Comment code location:", comment.markup_span.start, comment.markup_span.end)

```

# Parsers

| **Method** | **Use for** |
|--------------------|------------|
| `commie.iter_comments_c`| C99+, C++, Objective-C, C#, Java |
| `commie.iter_comments_js`| JavaScript, Dart |
| `commie.iter_comments_go`|Go|
| `commie.iter_comments_ruby` | Ruby |
| `commie.iter_comments_python` | Python |
| `commie.iter_comments_shell` | Bash, Sh |
| `commie.iter_comments_html` | HTML, XML, SGML |
| `commie.iter_comments_css` | CSS |


# Forked from [comment_parser](https://github.com/jeanralphaviles/comment_parser) 
Motivation:

| **comment_parser** | **commie** |
|--------------------|------------|
|Returned only a line number|Returns positions where the comment starts and ends. Just like regular string search|
|Returned only the text of a comment|Respects markup as well, making it possible to remove or replace the entire comment|
|Depends on [python-magic](https://pypi.org/project/python-magic) requiring an optional installation of binaries|Does not have this dependency|

