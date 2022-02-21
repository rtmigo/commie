[![PyPI version shields.io](https://img.shields.io/pypi/v/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI status](https://img.shields.io/pypi/status/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/commie.svg)](https://pypi.python.org/pypi/commie/)
[![Actions Status](https://github.com/rtmigo/commie.python/workflows/unit%20test/badge.svg?branch=master)](https://github.com/rtmigo/commie.python/actions)
[![Actions Status](https://github.com/rtmigo/commie.python/workflows/pkg%20test/badge.svg?branch=master)](https://github.com/rtmigo/commie.python/actions)

# [commie](https://github.com/rtmigo/commie)

Python package for **extracting comments** from source code.

Multiple programming and markup languages are
supported: [see list](https://github.com/rtmigo/commie.python#find-comments-in-a-string).

# Install

```sh
$ pip3 install commie
```

# Find comments in a file

``` python
from pathlib import Path
import commie

for comment in commie.iter_comments(Path("/path/to/source.cpp")):

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
| `commie.iter_comments_c`| C, C++, C#, Java, Objective-C, JavaScript, Dart, TypeScript |
| `commie.iter_comments_go`|Go|
| `commie.iter_comments_ruby` | Ruby |
| `commie.iter_comments_python` | Python |
| `commie.iter_comments_shell` | Bash, Sh |
| `commie.iter_comments_html` | HTML, XML, SGML |
| `commie.iter_comments_css` | CSS |
| `commie.iter_comments_sass` | SASS |

``` python
import commie

source_code_in_golang:str = ...

for comment in commie.iter_comments_go(source_code_in_golang):
    # ... process comment ...
    pass
```

# Find comments in a string with a known filename

Method `commie.iter_comments` will try to guess the file format from the provided filename.

``` python
from pathlib import Path
import commie

filename: str = "/path/to/mycode.go"
source_code: str = Path(filename).read_text()

for comment in commie.iter_comments(source_code, filename=filename):
    # ... process comment ...
    pass
```

# Group single line comments

When single-line comments are adjacent, it makes sense to consider them together:

```cpp
// Group A: A short comment

// Group B: It consists of three
// single-line comments with 
// no empty lines between them

// Group C: This paragraph loosely 
// stretched into two lines  
```

The comments from the example above can be combined into **three groups** as follows:

``` python
from commie import iter_comments, group_singleline_comments

for group in group_singleline_comments(iter_comments(...)):
    # ... each group is a list of Comment objects ...
    pass
```

Multi-line comments will also be returned. They will not be grouped with their neighbors.

# History

This project was forked from [comment_parser](https://github.com/jeanralphaviles/comment_parser) in 2021. Motivation:

| **comment_parser** | **commie** |
|--------------------|------------|
|Returns only a line number|Returns positions where the comment starts and ends. Just like regular string search|
|Returns only the text of a comment|Respects markup as well, making it possible to remove or replace the entire comment|
|Depends on [python-magic](https://pypi.org/project/python-magic) that requires an optional installation of binaries|Pure Python. Easy to install with `pip`|



