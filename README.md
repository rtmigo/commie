# [rtmigo / commie.python](https://github.com/rtmigo/commie.python/)
[![Actions Status](https://github.com/rtmigo/commie.python/workflows/CI/badge.svg?branch=master)](https://github.com/rtmigo/commie.python/actions)
[![PyPI status](https://img.shields.io/pypi/status/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI license](https://img.shields.io/pypi/l/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/commie.svg)](https://pypi.python.org/pypi/commie/)

# Find comments in a file

```python
from pathlib import Path
import commie

for comment in commie.iter_comments_file(Path("/path/to/source.cpp")):

  # something like "/* sample */"
  print("Comment code:", comment.code)
  print("Comment code location:", comment.code_span.start, comment.code_span.end)

  # something like " sample " 
  print("Comment inner text:", comment.text)
  print("Comment text location:", comment.text_span.start, comment.text_span.end)

```

# Find comments in a string

| **Method** | **Works for** |
|--------------------|------------|
| `commie.iter_comments_c`| C99+, C++, Objective-C, C#, Java |
| `commie.iter_comments_js`| JavaScript, Dart, TypeScript |
| `commie.iter_comments_go`|Go|
| `commie.iter_comments_ruby` | Ruby |
| `commie.iter_comments_python` | Python |
| `commie.iter_comments_shell` | Bash, Sh |
| `commie.iter_comments_html` | HTML, XML, SGML |
| `commie.iter_comments_css` | CSS |
| `commie.iter_comments_sass` | SASS |

```python
import commie

source_code_in_golang=loadSomehow(...)

for comment in commie.iter_comments_go(source_code_in_golang):
  # ... process comment ...
  pass
```

# Find comments in a string with a known filename

Method `commie.iter_comments` will try to guess the file format from the provided filename

```python
from pathlib import Path
import commie

filename = "/path/to/mycode.go"
source_code=Path(filename).read_text()

for comment in commie.iter_comments(source_code, filename):
  # ... process comment ...
  pass
```

# Forked from [comment_parser](https://github.com/jeanralphaviles/comment_parser) 

| **comment_parser** | **commie** |
|--------------------|------------|
|Returns only a line number|Returns positions where the comment starts and ends. Just like regular string search|
|Returns only the text of a comment|Respects markup as well, making it possible to remove or replace the entire comment|
|Depends on [python-magic](https://pypi.org/project/python-magic) requiring an optional installation of binaries|Does not have this dependency|

