[![Actions Status](https://github.com/rtmigo/commie.python/workflows/CI/badge.svg?branch=master)](https://github.com/rtmigo/commie.python/actions)
[![PyPI status](https://img.shields.io/pypi/status/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI license](https://img.shields.io/pypi/l/commie.svg)](https://pypi.python.org/pypi/commie/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/commie.svg)](https://pypi.python.org/pypi/commie/)

A fork from [comment_parser](https://github.com/jeanralphaviles/comment_parser). 
Motivation:

| **comment_parser** | **commie** |
|--------------------|------------|
|Returned only a line number|Returns positions where the comment starts and ends. Just like regular string search|
|Returned only the text of a comment|Respects markup as well, making it possible to remove or replace the entire comment|
|Depends on [python-magic](https://pypi.org/project/python-magic) requiring an optional installation of binaries|Does not have this dependency|

